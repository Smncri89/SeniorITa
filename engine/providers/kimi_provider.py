# -*- coding: utf-8 -*-

import requests

from engine.secrets_manager import SecretsManager


class KimiProvider:

    def __init__(
        self,
        model="moonshot-v1-8k"
    ):

        self.model = model

        secrets = SecretsManager()

        self.api_key = secrets.get_kimi_key().strip()

        self.url = (
            "https://api.moonshot.ai/v1/chat/completions"
        )


    def generate(self, prompt):

        try:

            response = requests.post(
                self.url,
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": self.model,
                    "messages": [
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                },
                timeout=60
            )

            if response.status_code != 200:
                return {
                    "provider": "kimi",
                    "model": self.model,
                    "status_code": response.status_code,
                    "error": response.text
                }

            data = response.json()

            return {
                "provider": "kimi",
                "model": self.model,
                "response": data["choices"][0]["message"]["content"]
            }


        except Exception as e:

            return {
                "provider": "kimi",
                "model": self.model,
                "error": str(e)
            }