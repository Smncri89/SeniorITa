# -*- coding: utf-8 -*-

from engine.providers.ollama_provider import OllamaProvider
from engine.providers.coder_provider import CoderProvider


class ProviderFactory:

    @staticmethod
    def create(provider, model=None):

        providers = {
            "ollama": OllamaProvider,
            "coder": CoderProvider,
        }

        if provider not in providers:
            raise Exception(
                f"Provider non supportato: {provider}"
            )

        provider_class = providers[provider]

        if model:
            return provider_class(model=model)

        return provider_class()