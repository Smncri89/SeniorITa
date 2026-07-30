# -*- coding: utf-8 -*-


from abc import ABC, abstractmethod



class LLMProvider(ABC):


    @abstractmethod
    def generate(self, prompt):

        pass