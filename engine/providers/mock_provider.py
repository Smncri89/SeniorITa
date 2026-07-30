# -*- coding: utf-8 -*-


class MockProvider:


    def generate(self, prompt):

        return {
            "provider": "mock",
            "response": "LLM response placeholder",
            "prompt_received": prompt
        }