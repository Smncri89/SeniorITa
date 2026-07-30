# -*- coding: utf-8 -*-

class IntentAnalyzer:

    def analyze(self, request: str):

        text = request.lower()

        intent = "generic"
        workflow = "standard"
        complexity = "low"
        domain = "general"

        if any(word in text for word in [
            "jwt",
            "oauth",
            "security",
            "sicurezza",
            "vulnerabilità",
            "vulnerabilita",
            "token",
            "xss",
            "csrf",
            "sql injection"
        ]):

            intent = "security_review"
            workflow = "security_review"
            domain = "security"
            complexity = "high"

        elif any(word in text for word in [
            "python",
            "java",
            "api",
            "feature",
            "bug",
            "refactor",
            "codice",
            "funzione",
            "classe"
        ]):

            intent = "implementation"
            workflow = "feature_development"
            domain = "software"
            complexity = "medium"

        elif any(word in text for word in [
            "docker",
            "kubernetes",
            "deploy",
            "pipeline",
            "terraform"
        ]):

            intent = "deployment"
            workflow = "deployment"
            domain = "devops"
            complexity = "medium"

        return {

            "intent": intent,
            "workflow": workflow,
            "domain": domain,
            "complexity": complexity

        }