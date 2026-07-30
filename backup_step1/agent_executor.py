# -*- coding: utf-8 -*-

from engine.providers.provider_factory import ProviderFactory
from engine.prompt_loader import PromptLoader


class AgentExecutor:

    def __init__(
        self,
        provider="ollama"
    ):
        self.provider_name = provider

    def execute(
        self,
        agent,
        request
    ):

        model = agent.get("model")

        provider = ProviderFactory.create(
            self.provider_name,
            model
        )

        system_prompt = PromptLoader.load(
            agent["file"]
        )

        prompt = f"""
{system_prompt}

----------------------------------------------------

User request:

{request}

----------------------------------------------------

Follow all the instructions above.

Think step by step.

Produce enterprise-grade output.

If code is required:
- explain choices
- provide complete code
- highlight risks
"""

        llm_result = provider.generate(prompt)

        return {
            "agent": agent["name"],
            "provider": llm_result["provider"],
            "model": llm_result["model"],
            "request": request,
            "instructions_loaded": True,
            "llm_response": llm_result
        }