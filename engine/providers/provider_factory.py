# -*- coding: utf-8 -*-

from engine.providers.ollama_provider import OllamaProvider
from engine.providers.coder_provider import CoderProvider
from engine.providers.xai_provider import XAIProvider
from engine.providers.gemini_provider import GeminiProvider
from engine.providers.kimi_provider import KimiProvider


class ProviderFactory:

    _PROVIDERS = {
        "ollama": OllamaProvider,
        "coder": CoderProvider,
        "xai": XAIProvider,
        "gemini": GeminiProvider,
        "kimi": KimiProvider,
    }

    @classmethod
    def create(cls, provider, model=None):

        provider = provider.lower().strip()

        if provider not in cls._PROVIDERS:
            available = ", ".join(sorted(cls._PROVIDERS.keys()))
            raise ValueError(
                f"Provider '{provider}' non supportato. "
                f"Provider disponibili: {available}"
            )

        provider_class = cls._PROVIDERS[provider]

        if model:
            return provider_class(model=model)

        return provider_class()

    @classmethod
    def supported_providers(cls):
        return sorted(cls._PROVIDERS.keys())

    @classmethod
    def exists(cls, provider):
        return provider.lower().strip() in cls._PROVIDERS