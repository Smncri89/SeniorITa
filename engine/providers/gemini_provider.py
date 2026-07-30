# -*- coding: utf-8 -*-

import requests

from engine.secrets_manager import SecretsManager



class GeminiProvider:


    def __init__(
        self,
        model="gemini-2.0-flash"
    ):

        self.model = model

        secrets = SecretsManager()

        self.api_key = secrets.get_gemini_key()


        self.url = (
            "https://generativelanguage.googleapis.com/v1beta/"
            f"models/{self.model}:generateContent"
        )



    def generate(
        self,
        prompt
    ):


        if not self.api_key:

            raise Exception(
                "GEMINI_API_KEY mancante"
            )



        payload = {

            "contents": [

                {

                    "role": "user",

                    "parts": [

                        {

                            "text":
                            """
Rispondi sempre in italiano.
Usa stile tecnico enterprise.

""" + prompt

                        }

                    ]

                }

            ]

        }



        response = requests.post(

            self.url,

            params={

                "key": self.api_key

            },

            json=payload,

            timeout=120

        )



        if response.status_code != 200:

            print(
                "ERRORE GEMINI:"
            )

            print(
                response.text
            )

            response.raise_for_status()



        data = response.json()



        return {

            "provider": "gemini",

            "model": self.model,

            "response":
            data["candidates"][0]["content"]["parts"][0]["text"],

            "prompt_received": prompt

        }