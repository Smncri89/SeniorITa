# -*- coding: utf-8 -*-

import os

from dotenv import load_dotenv


load_dotenv()



class SecretsManager:


    def get_gemini_key(self):

        return os.getenv(
            "GEMINI_API_KEY"
        )



    def get_kimi_key(self):

        return os.getenv(
            "KIMI_API_KEY"
        )



    def get_groq_key(self):

        return os.getenv(
            "GROQ_API_KEY"
        )



    def get_xai_key(self):

        return os.getenv(
            "XAI_API_KEY"
        )