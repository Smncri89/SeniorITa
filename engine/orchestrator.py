# -*- coding: utf-8 -*-

from engine.planner import Planner
from engine.workflow import WorkflowEngine
from engine.workflow_runner import WorkflowRunner
from engine.model_router import ModelRouter
from engine.providers.provider_factory import ProviderFactory


class Orchestrator:

    def __init__(self):

        self.planner = Planner()
        self.workflow = WorkflowEngine()
        self.runner = WorkflowRunner()

        # Nuovi componenti AI
        self.router = ModelRouter()

    def handle_request(self, request):

        # ==========================
        # ANALISI DELLA RICHIESTA
        # ==========================

        plan = self.planner.plan(request)

        agent = plan["agent"]

        analysis = plan["analysis"]


        # ==========================
        # ROUTING DEL MODELLO AI
        # ==========================

        ai = self.router.select_model(
            request=request,
            agent=agent
        )


        # ==========================
        # WORKFLOW
        # ==========================

        workflow = self.workflow.get_workflow(
            analysis["workflow"]
        )


        # ==========================
        # ESECUZIONE WORKFLOW
        # ==========================

        execution = self.runner.run(
            workflow,
            request
        )


        # ==========================
        # OUTPUT
        # ==========================

        return {

            "request": request,

            "analysis": analysis,

            "agent": agent,

            "workflow": workflow,

            "selected_ai": ai,

            "execution": execution

        }


    def create_provider(self, provider, model=None):
        """
        Factory centralizzata.
        In futuro verrà usata per fallback,
        retry e load balancing.
        """

        return ProviderFactory.create(
            provider,
            model
        )S