# -*- coding: utf-8 -*-
import json
import subprocess
from pathlib import Path
from engine.intent_analyzer import IntentAnalyzer
from engine.audit import AuditLogger

class TaskPlanner:
    def __init__(self, ps_script_name: str = "run_intent.ps1"):
        self.project_root = Path(__file__).resolve().parent.parent
        self.ps_script_path = self.project_root / ps_script_name
        self.analyzer = IntentAnalyzer()
        self.audit = AuditLogger()

    def execute_prompt(self, prompt: str):
        print(f"\n?? SeniorITa Agent | Richiesta: '{prompt}'")
        print("=" * 60)
        
        # 1. Analisi dell'intent e generazione del payload JSON
        intent_data = self.analyzer.analyze(prompt)
        json_payload = json.dumps(intent_data)

        # 2. Verifica presenza dello script PowerShell
        if not self.ps_script_path.exists():
            err_msg = f"Script PowerShell non trovato in '{self.ps_script_path}'"
            print(f"? ERRORE: {err_msg}")
            self.audit.log_event(prompt, intent_data, status="FAILED", details=err_msg)
            return

        # 3. Invocazione di PowerShell tramite subprocess
        cmd = [
            "powershell.exe",
            "-ExecutionPolicy", "Bypass",
            "-File", str(self.ps_script_path),
            "-JsonInput", json_payload
        ]

        # 4. Esecuzione interattiva e Logging
        try:
            process = subprocess.Popen(cmd)
            exit_code = process.wait()
            
            if exit_code == 0:
                self.audit.log_event(prompt, intent_data, status="COMPLETED")
            else:
                self.audit.log_event(prompt, intent_data, status="ABORTED_OR_FAILED", details=f"Exit code: {exit_code}")
        except Exception as e:
            print(f"? Errore durante l'esecuzione dello script: {e}")
            self.audit.log_event(prompt, intent_data, status="ERROR", details=str(e))
