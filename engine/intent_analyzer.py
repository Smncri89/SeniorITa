# -*- coding: utf-8 -*-
from typing import Dict, Any
from dataclasses import dataclass, field, asdict

@dataclass
class IntentResult:
    intent: str               # ID della capability/workflow (es. "ad.join_domain")
    domain: str               # "active_directory", "m365", "system", "network", "devops"
    workflow: str             # Il workflow associato nel Task Planner
    complexity: str           # "low", "medium", "high", "critical"
    risk_level: str           # "LOW", "MEDIUM", "HIGH", "CRITICAL"
    requires_approval: bool   # Se serve sblocco/conferma prima di eseguire
    parameters: Dict[str, Any] = field(default_factory=dict)

class IntentAnalyzer:
    """
    Analizzatore degli intenti per SeniorITa Autonomous IT Operations Platform.
    Classifica le richieste in arrivo dall'operatore in azioni infrastrutturali deterministiche.
    """

    def analyze(self, request: str) -> Dict[str, Any]:
        text = request.lower().strip()

        # Defaults
        intent = "system.generic_query"
        workflow = "knowledge_retrieval"
        domain = "general"
        complexity = "low"
        risk_level = "LOW"
        requires_approval = False
        params = {"raw_request": request}

        # -------------------------------------------------------------
        # 1. ACTIVE DIRECTORY & IDENTITY
        # -------------------------------------------------------------
        if any(word in text for word in ["join", "dominio", "domain join", "aggiungi a dominio"]):
            intent = "ad.join_domain"
            workflow = "domain_join_workflow"
            domain = "active_directory"
            complexity = "high"
            risk_level = "HIGH"
            requires_approval = True

        elif any(word in text for word in ["reset password", "sblocca utente", "sblocca account", "unlock account"]):
            intent = "ad.reset_password"
            workflow = "identity_reset_workflow"
            domain = "active_directory"
            complexity = "medium"
            risk_level = "MEDIUM"
            requires_approval = False

        elif any(word in text for word in ["crea utente", "nuovo dipendente", "onboarding utente", "onboard"]):
            intent = "ad.create_user"
            workflow = "user_onboarding_workflow"
            domain = "active_directory"
            complexity = "high"
            risk_level = "HIGH"
            requires_approval = True

        # -------------------------------------------------------------
        # 2. MICROSOFT 365 / EXCHANGE / LICENSING
        # -------------------------------------------------------------
        elif any(word in text for word in ["licenza m365", "assegna licenza", "m365 license", "mailbox"]):
            intent = "m365.manage_license"
            workflow = "m365_licensing_workflow"
            domain = "microsoft_365"
            complexity = "medium"
            risk_level = "MEDIUM"
            requires_approval = False

        # -------------------------------------------------------------
        # 3. ASSET INVENTORY & HARDWARE / SYSTEM AUDIT
        # -------------------------------------------------------------
        elif any(word in text for word in ["inventario", "asset", "hardware", "tpm", "bitlocker", "audit host"]):
            intent = "system.asset_inventory"
            workflow = "inventory_audit_workflow"
            domain = "system"
            complexity = "low"
            risk_level = "LOW"
            requires_approval = False

        # -------------------------------------------------------------
        # 4. NETWORK & DIAGNOSTICS
        # -------------------------------------------------------------
        elif any(word in text for word in ["ping", "dns", "connettività", "porta", "firewall", "reachability"]):
            intent = "network.diagnose"
            workflow = "network_diagnostic_workflow"
            domain = "network"
            complexity = "low"
            risk_level = "LOW"
            requires_approval = False

        # -------------------------------------------------------------
        # 5. SECURITY & VULNERABILITY
        # -------------------------------------------------------------
        elif any(word in text for word in ["jwt", "oauth", "security", "sicurezza", "vulnerabilità", "vulnerabilita", "token", "xss", "csrf", "sql injection"]):
            intent = "security_review"
            workflow = "security_review_workflow"
            domain = "security"
            complexity = "high"
            risk_level = "HIGH"
            requires_approval = True

        result = IntentResult(
            intent=intent,
            domain=domain,
            workflow=workflow,
            complexity=complexity,
            risk_level=risk_level,
            requires_approval=requires_approval,
            parameters=params
        )

        return asdict(result)

if __name__ == "__main__":
    analyzer = IntentAnalyzer()
    print("--- Test 1: Join Dominio ---")
    print(analyzer.analyze("Metti questo PC nel dominio corp.internal"))
    print("\n--- Test 2: Asset Inventory ---")
    print(analyzer.analyze("Fammi l'inventario hardware e BitLocker della macchina"))