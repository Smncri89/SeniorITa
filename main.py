# -*- coding: utf-8 -*-
import sys
from engine.planner import TaskPlanner

def print_banner():
    banner = """
    ==========================================================
              SeniorITa - Autonomous IT Operations            
    ==========================================================
    Digitare 'exit' o 'quit' per uscire.
    """
    print(banner)

def main():
    print_banner()
    planner = TaskPlanner()

    while True:
        try:
            prompt = input("SeniorITa> ").strip()
            if not prompt:
                continue
            
            if prompt.lower() in ["exit", "quit", "q"]:
                print("\nChiusura della sessione SeniorITa. Arrivederci!\n")
                break

            planner.execute_prompt(prompt)
            print("\n" + "-" * 60 + "\n")

        except (KeyboardInterrupt, EOFError):
            print("\n\nSessione interrotta. Uscita...")
            sys.exit(0)

if __name__ == "__main__":
    main()
