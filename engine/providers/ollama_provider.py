# -*- coding: utf-8 -*-

import requests


class OllamaProvider:

    def __init__(
        self,
        model="seniorita-qwen",
        url="http://localhost:11434"
):
        self.model = model
        self.url = url


    def generate(self, prompt):

        response = requests.post(
            f"{self.url}/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        response.raise_for_status()

        data = response.json()

        return {
            "provider": "ollama",
            "model": self.model,
            "response": data.get("response", ""),
            "prompt_received": prompt
        }