# -*- coding: utf-8 -*-

import requests

from engine.secrets_manager import SecretsManager



class XAIProvider:


    def __init__(
        self,
        model="grok-3-mini"
    ):

        self.model = model

        secrets = SecretsManager()

        self.api_key = secrets.get_xai_key()

        self.url = (
            "https://api.x.ai/v1/chat/completions"
        )



    def generate(
        self,
        prompt
    ):


        response = requests.post(

            self.url,

            headers={

                "Authorization":
                f"Bearer {self.api_key}",

                "Content-Type":
                "application/json"

            },

            json={

                "model": self.model,

                "messages":[
                    {
                        "role":"user",
                        "content":prompt
                    }
                ]

            },

            timeout=120

        )


        response.raise_for_status()


        data=response.json()


        return {

            "provider":"xai",

            "model":self.model,

            "response":
            data["choices"][0]["message"]["content"]

        }
    