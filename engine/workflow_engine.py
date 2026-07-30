# -*- coding: utf-8 -*-

from engine.agent_executor import AgentExecutor
from engine.registry import AgentRegistry


class WorkflowEngine:

    def __init__(self):

        self.registry = AgentRegistry()

    def execute(
        self,
        workflow,
        request
    ):

        results = []

        context = request

        for step in workflow:

            agent = self.registry.get_agent(step["agent"])

            executor = AgentExecutor(
                provider=step["provider"],
                model=step["model"]
            )

            result = executor.execute(
                agent,
                context
            )

            results.append(result)

            context = result["llm_response"]["response"]

        return results