# -*- coding: utf-8 -*-

import os

from dotenv import load_dotenv


load_dotenv()



class SecretsManager:


    def get_gemini_key(self):

        return os.getenv(
            "GEMINI_API_KEY"
        )



    def get_claude_key(self):

        return os.getenv(
            "CLAUDE_API_KEY"
        )



    def get_openai_key(self):

        return os.getenv(
            "OPENAI_API_KEY"
        )