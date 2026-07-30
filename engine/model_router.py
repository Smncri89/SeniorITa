# -*- coding: utf-8 -*-


class ModelRouter:

    def __init__(self):

        self.routes = [

            {
                "name": "coding",

                "provider": "coder",

                "model": "qwen2.5-coder:7b",

                "reason": "complex_code_task",

                "keywords": [

                    "implementa",
                    "sviluppa",
                    "sviluppare",
                    "crea codice",
                    "scrivi codice",
                    "python",
                    "javascript",
                    "java",
                    "c#",
                    "c++",
                    "go",
                    "rust",
                    "php",
                    "sql",
                    "database",
                    "mongodb",
                    "postgres",
                    "mysql",
                    "api",
                    "rest",
                    "jwt",
                    "oauth",
                    "docker",
                    "kubernetes",
                    "microservizio",
                    "debug",
                    "bug",
                    "refactor",
                    "refactoring",
                    "unit test",
                    "framework"

                ]

            },


            {
                "name": "enterprise",

                "provider": "xai",

                "model": "grok-3-mini",

                "reason": "enterprise_reasoning",

                "keywords": [

                    "enterprise",
                    "architettura",
                    "architecture",
                    "cloud",
                    "azure",
                    "aws",
                    "gcp",
                    "active directory",
                    "entra",
                    "exchange",
                    "microsoft 365",
                    "vpn",
                    "network",
                    "firewall",
                    "server",
                    "windows server",
                    "linux",
                    "infrastruttura",
                    "scalabilità",
                    "design",
                    "strategia"

                ]

            },


            {
                "name": "security",

                "provider": "ollama",

                "model": "seniorita-qwen",

                "reason": "security_reasoning",

                "keywords": [

                    "sicurezza",
                    "security",
                    "vulnerability",
                    "vulnerabilità",
                    "pentest",
                    "penetration",
                    "gdpr",
                    "soc",
                    "siem",
                    "edr",
                    "crowdstrike",
                    "authentication",
                    "autenticazione",
                    "authorization",
                    "token"

                ]

            }

        ]



    def select_model(
        self,
        request,
        agent=None
    ):

        text = request.lower()

        for route in self.routes:

            if any(
                keyword in text
                for keyword in route["keywords"]
            ):

                return {

                    "provider": route["provider"],

                    "model": route["model"],

                    "reason": route["reason"]

                }

        return {

            "provider": "ollama",

            "model": "seniorita-qwen",

            "reason": "general_reasoning"

        }