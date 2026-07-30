# -*- coding: utf-8 -*-

import requests

from engine.secrets_manager import SecretsManager


class GroqProvider:


    def __init__(
        self,
        model="llama-3.3-70b-versatile"
    ):

        self.model = model
        self.url = "https://api.groq.com/openai/v1/chat/completions"

        self.secrets = SecretsManager()

        self.api_key = self.secrets.get_groq_key()


    def generate(self, prompt):


        if not self.api_key:
            raise Exception(
                "GROQ_API_KEY mancante"
            )


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
                ],

                "temperature": 0.2

            },

            timeout=120

        )


        response.raise_for_status()


        data = response.json()


        return {

            "provider": "groq",

            "model": self.model,

            "response":
                data["choices"][0]["message"]["content"],

            "prompt_received": prompt

        }