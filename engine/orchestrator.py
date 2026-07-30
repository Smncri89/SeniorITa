# -*- coding: utf-8 -*-

from engine.registry import AgentRegistry
from engine.workflow import WorkflowEngine
from engine.workflow_runner import WorkflowRunner


class Orchestrator:


    def __init__(self):

        self.registry = AgentRegistry()
        self.workflow = WorkflowEngine()
        self.runner = WorkflowRunner()



    def analyze_request(self, request):

        request = request.lower()


        rules = {

            "security": [
                "vulnerabilità",
                "security",
                "sicurezza",
                "authentication",
                "token",
                "api"
            ],

            "developer": [
                "bug",
                "errore",
                "feature",
                "sviluppo",
                "codice",
                "refactoring"
            ],

            "devops": [
                "deploy",
                "pipeline",
                "ci/cd",
                "automazione",
                "deployment"
            ],

            "test": [
                "test",
                "qualità",
                "regressione",
                "validation"
            ],

            "documentation": [
                "documentazione",
                "manuale",
                "readme",
                "document"
            ],

            "architect": [
                "architettura",
                "design",
                "scalabilità",
                "sistema"
            ]

        }


        for agent_name, keywords in rules.items():

            for keyword in keywords:

                if keyword in request:

                    return self.registry.get_agent(agent_name)


        return self.registry.get_agent("architect")



    def determine_workflow(self, request):

        request = request.lower()


        if any(word in request for word in [
            "vulnerabilità",
            "security",
            "sicurezza",
            "authentication",
            "token",
            "api"
        ]):

            return "security_fix"



        if any(word in request for word in [
            "feature",
            "sviluppo",
            "nuova funzionalità",
            "codice",
            "refactoring"
        ]):

            return "feature_development"



        if any(word in request for word in [
            "deploy",
            "pipeline",
            "ci/cd",
            "automazione",
            "deployment"
        ]):

            return "deployment"



        return "standard"



    def handle_request(self, request):


        agent = self.analyze_request(request)


        workflow_name = self.determine_workflow(request)


        workflow = self.workflow.get_workflow(
            workflow_name
        )


        execution = self.runner.run(
            workflow,
            request
        )


        return {

            "request": request,

            "initial_agent": agent["name"],

            "role": agent["role"],

            "capabilities": agent["capabilities"],

            "workflow": workflow,

            "execution": execution

        }