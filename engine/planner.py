# -*- coding: utf-8 -*-

from engine.intent_analyzer import IntentAnalyzer
from engine.registry import AgentRegistry


class Planner:

    def __init__(self):

        self.intent = IntentAnalyzer()
        self.registry = AgentRegistry()

        # Mappa dominio -> agente
        self.domain_mapping = {

            "security": "security",

            "software": "developer",

            "devops": "devops",

            "network": "network",

            "cloud": "cloud",

            "windows": "windows",

            "linux": "linux",

            "database": "database",

            "architecture": "architect"

        }

        self.default_agent = "architect"

    def plan(self, request):

        analysis = self.intent.analyze(request)

        domain = analysis.get(
            "domain",
            ""
        ).lower()

        agent_name = self.domain_mapping.get(
            domain,
            self.default_agent
        )

        agent = self.registry.get_agent(
            agent_name
        )

        return {

            "analysis": analysis,

            "agent": agent,

            "selected_agent": agent_name

        }