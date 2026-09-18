import os
import sys
import re
import json
import time
import logging
import subprocess
import urllib.request
import urllib.error
from pathlib import Path

LOG_FILE_PATH = os.path.join("logs", "execution.log")
SCRIPTS_DIR = Path("scripts")
MAX_HEALING_ATTEMPTS = 2

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434")

# Manteniamo i modelli dal più nuovo al più vecchio
GEMINI_MODELS = ["gemini-3.6-flash", "gemini-2.5-flash", "gemini-2.0-flash", "gemini-1.5-flash"]
GROQ_MODELS = ["llama-3.3-70b-versatile", "qwen-2.5-coder-32b"]
OLLAMA_MODEL = "qwen2.5-coder"

os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True)
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

def is_direct_powershell(text: str) -> bool:
    t = text.strip()
    cmdlet_pattern = r"^(get|set|test|new|remove|start|stop|restart|enable|disable|invoke|select|where|out|format)-[a-z0-9]+"
    alias_pattern = r"^(dir|ls|cat|type|cd|pwd|ps|gps|gc|ipconfig|ping|tracert|netstat|whoami|hostname|systeminfo|cls|clear)(\s|$)"
    if re.match(cmdlet_pattern, t, re.IGNORECASE) or re.match(alias_pattern, t, re.IGNORECASE):
        return True
    if t.startswith(".\\") or t.startswith("./") or t.startswith("&"):
        return True
    return False

def get_available_tools_prompt():
    tools = []
    if SCRIPTS_DIR.exists():
        for ps_file in SCRIPTS_DIR.glob("*.ps1"):
            tools.append(f"- {ps_file.name}: Script consolidato per automazione locale.")
    return "\n".join(tools) if tools else "Nessuno script locale registrato."

def build_system_prompt():
    available_tools = get_available_tools_prompt()
    return f"""Sei SeniorITa, un Assistente IT Senior specializzato in amministrazione di sistema Windows e automazione PowerShell.

STRUMENTI LOCALI DISPONIBILI NELLA CARTELLA scripts/:
{available_tools}

REGOLE TASSATIVE DI RISPOSTA:
Rispondi ESCLUSIVAMENTE con un oggetto JSON valido, completo e non troncato.
Formato JSON:
{{
  "action": "tool" | "adhoc" | "message",
  "tool_name": "NomeFile.ps1 se action e tool",
  "parameters": "parametri opzionali per il tool",
  "powershell_code": "codice PowerShell 5.1 completo se action e adhoc",
  "summary": "breve spiegazione tecnica in italiano"
}}

LINEE GUIDA:
1. Per scansioni di rete, dispositivi connessi, MAC OUI o stato VPN usa SEMPRE: action="tool", tool_name="Scan-Network.ps1".
2. Per richieste su stato dischi, CPU, RAM, processi, utenti, porte o log usa SEMPRE: action="adhoc" e formatta a video.
3. Se l'utente saluta o fa domande teoriche usa: action="message".
"""

def call_gemini(messages, api_key):
    for model in GEMINI_MODELS:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
        contents = []
        for m in messages:
            if m["role"] == "system": continue
            role = "user" if m["role"] == "user" else "model"
            contents.append({"role": role, "parts": [{"text": m["content"]}]})
        
        payload = {
            "system_instruction": {"parts": [{"text": build_system_prompt()}]},
            "contents": contents,
            "generationConfig": {"temperature": 0.1, "maxOutputTokens": 4096}
        }
        data_encoded = json.dumps(payload).encode("utf-8")
        
        # Sistema di RETRY integrato per i 503
        for attempt in range(3):
            req = urllib.request.Request(url, data=data_encoded, headers={"Content-Type": "application/json"})
            try:
                with urllib.request.urlopen(req, timeout=20) as resp:
                    data = json.loads(resp.read().decode("utf-8"))
                    return data["candidates"][0]["content"]["parts"][0]["text"], f"Gemini ({model})"
            except urllib.error.HTTPError as e:
                err_str = e.read().decode("utf-8", errors="ignore")
                if e.code in (503, 429):
                    if attempt < 2:
                        print(f"\r [Google API occupata ({e.code}), ritento in 2s... ({attempt+1}/3)] ", end="", flush=True)
                        time.sleep(2)
                        continue
                    else:
                        break # Finiti i tentativi, passa al prossimo modello
                elif e.code == 404:
                    break # Modello deprecato, passa subito al prossimo
                elif e.code == 400:
                    print(f"\n[ERRORE SINTASSI API]: La chiave o il payload non sono validi.")
                    return None, None
                else:
                    logging.error(f"Gemini HTTP {e.code}: {err_str}")
                    print(f"\n[ERRORE GEMINI {e.code}]: {err_str}")
                    break
            except Exception as e:
                print(f"\n[ERRORE DI RETE/TIMEOUT]: {e}")
                break
    return None, None

def call_groq(messages, api_key):
    for model in GROQ_MODELS:
        url = "https://api.groq.com/openai/v1/chat/completions"
        groq_msgs = [{"role": "system", "content": build_system_prompt()}] + [m for m in messages if m["role"] != "system"]
        payload = {
            "model": model,
            "messages": groq_msgs,
            "temperature": 0.1,
            "response_format": {"type": "json_object"}
        }
        req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        })
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return data["choices"][0]["message"]["content"], f"Groq ({model})"
        except Exception:
            continue
    return None, None

def call_ollama(messages):
    url = f"{OLLAMA_URL}/api/chat"
    ollama_msgs = [{"role": "system", "content": build_system_prompt()}] + [m for m in messages if m["role"] != "system"]
    payload = {
        "model": OLLAMA_MODEL,
        "messages": ollama_msgs,
        "stream": False,
        "format": "json",
        "options": {"temperature": 0.1, "num_ctx": 4096}
    }
    req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data["message"]["content"], f"Ollama ({OLLAMA_MODEL})"
    except Exception:
        return None, None

def query_resilient_llm(messages):
    api_key_gemini = os.environ.get("GEMINI_API_KEY", "") or GEMINI_API_KEY
    api_key_groq = os.environ.get("GROQ_API_KEY", "") or GROQ_API_KEY

    if not api_key_gemini and not api_key_groq:
        print("\n[ATTENZIONE] Nessuna API Key trovata. Verrà utilizzato solo il modello locale Ollama se attivo.")

    if api_key_gemini:
        res, provider = call_gemini(messages, api_key_gemini)
        if res: return res, provider

    if api_key_groq:
        res, provider = call_groq(messages, api_key_groq)
        if res: return res, provider

    res, provider = call_ollama(messages)
    if res: return res, provider

    return None, None

def parse_llm_json(raw_text):
    if not raw_text: return None
    clean = re.sub(r"^```(?:json)?\s*", "", raw_text.strip(), flags=re.IGNORECASE)
    clean = re.sub(r"\s*```$", "", clean)
    try:
        return json.loads(clean)
    except Exception:
        match = re.search(r"\{.*\}", clean, re.DOTALL)
        if match:
            try: return json.loads(match.group(0))
            except Exception: pass
        if clean.startswith("{") and not clean.endswith("}"):
            for suffix in ['"}', '"]}', '}']:
                try:
                    return json.loads(clean + suffix)
                except Exception:
                    continue
    return None

def run_powershell_code(code):
    try:
        res = subprocess.run(
            ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", code],
            capture_output=True,
            text=True,
            encoding="oem"
        )
        return res.returncode, res.stdout.strip(), res.stderr.strip()
    except Exception as e:
        return -1, "", str(e)

def execute_with_auto_healing(code, history, provider_name):
    current_code = code
    for attempt in range(MAX_HEALING_ATTEMPTS + 1):
        retcode, out, err = run_powershell_code(current_code)
        
        if out:
            print(out)
            
        if retcode == 0 and not (err and "Errore" in err):
            if attempt > 0:
                print(f"[OK] Comando corretto al tentativo {attempt}!")
            return True

        if attempt < MAX_HEALING_ATTEMPTS:
            print(f"\n[AUTO-HEALING] Errore di esecuzione. Tento la correzione ({attempt + 1}/{MAX_HEALING_ATTEMPTS})...")
            heal_prompt = "Il comando ha generato errore: " + err + "\nCorreggi il codice PowerShell 5.1 e rispondi ESCLUSIVAMENTE in JSON valido con action='adhoc'."
            history.append({"role": "user", "content": heal_prompt})
            fixed_resp, _ = query_resilient_llm(history)
            if not fixed_resp: break
            parsed = parse_llm_json(fixed_resp)
            if not parsed or not parsed.get("powershell_code"): break
            current_code = parsed["powershell_code"]
        else:
            if err:
                print(f"\n[ERRORE]: {err}")
    return False

def main():
    print("="*65)
    print(" SeniorITa - IT Operations Assistant (Smart Pass-Through Attivo)")
    print(" Modalità: Linguaggio naturale (AI) | Comandi PowerShell diretti")
    print(" Digita 'exit' per uscire | 'clear' per azzerare il contesto")
    print("="*65)

    history = []
    
    while True:
        try:
            user_input = input("\nSeniorITa> ").strip()
            if not user_input: continue
            if user_input.lower() in ["exit", "quit"]: break
            if user_input.lower() in ["clear", "reset", "cls"]:
                history = []
                os.system("cls" if os.name == "nt" else "clear")
                print("="*65 + "\n Memoria pulita e contesto azzerato.\n" + "="*65)
                continue

            # Intercettazione comandi PowerShell diretti
            if is_direct_powershell(user_input):
                ret, out, err = run_powershell_code(user_input)
                if out: print(out)
                if err: print(f"[AVVISO/ERRORE]: {err}")
                continue

            history.append({"role": "user", "content": user_input})
            if len(history) > 8: history = history[-8:]

            print("\n [Elaborazione in corso...]", end="", flush=True)
            raw_response, provider = query_resilient_llm(history)
            print("\r" + " " * 45 + "\r", end="")

            if not raw_response:
                print("[ERRORE FINALE] Nessun provider AI raggiungibile. Server sovraccarichi o disconnessi.")
                continue

            parsed = parse_llm_json(raw_response)
            if not parsed:
                print(f"\nSeniorITa ({provider}): {raw_response}\n")
                continue

            action = parsed.get("action", "message")
            summary = parsed.get("summary", "")
            if summary:
                print(f"[{provider}] {summary}\n")

            if action == "tool":
                tool_name = parsed.get("tool_name", "")
                params = parsed.get("parameters", "")
                tool_path = SCRIPTS_DIR / tool_name
                if tool_path.exists():
                    cmd = f"& '{tool_path.resolve()}' {params}"
                    ret, out, err = run_powershell_code(cmd)
                    if out: print(out)
                    if err: print(f"[AVVISO]: {err}")
                else:
                    print(f"[ERRORE TOOL]: Lo script {tool_name} non esiste in {SCRIPTS_DIR}.")

            elif action == "adhoc":
                code = parsed.get("powershell_code", "")
                if code:
                    execute_with_auto_healing(code, history, provider)
                else:
                    print("[ERRORE]: Nessun codice generato.")

            elif action == "message":
                print(f"{parsed.get('summary', '')}")

        except KeyboardInterrupt:
            print("\nOperazione interrotta.")
            break
        except Exception as e:
            print(f"\n[ECCEZIONE]: {e}")
            logging.error(f"Errore: {e}")

if __name__ == "__main__":
    main()
