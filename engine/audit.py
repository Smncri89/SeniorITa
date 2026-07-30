# -*- coding: utf-8 -*-
import json
from datetime import datetime
from pathlib import Path

class AuditLogger:
    def __init__(self, log_dir: str = "logs"):
        self.project_root = Path(__file__).resolve().parent.parent
        self.log_path = self.project_root / log_dir
        self.log_path.mkdir(exist_ok=True)
        self.log_file = self.log_path / "audit.log"

    def log_event(self, prompt: str, intent_data: dict, status: str = "EXECUTED", details: str = ""):
        event = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "prompt": prompt,
            "intent": intent_data.get("intent"),
            "domain": intent_data.get("domain"),
            "workflow": intent_data.get("workflow"),
            "risk_level": intent_data.get("risk_level"),
            "requires_approval": intent_data.get("requires_approval"),
            "status": status,
            "details": details
        }
        
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(event, ensure_ascii=False) + "\n")
