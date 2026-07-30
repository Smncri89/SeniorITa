# -*- coding: utf-8 -*-

from pathlib import Path
import yaml



class ConfigManager:


    def __init__(self):

        self.config_file = (
            Path(__file__)
            .parent
            .parent
            / "config"
            / "llm_config.yaml"
        )


        self.config = self.load()



    def load(self):

        with open(
            self.config_file,
            "r",
            encoding="utf-8"
        ) as file:

            return yaml.safe_load(file)



    def get_default_provider(self):

        return self.config.get(
            "default_provider",
            "mock"
        )



    def get_provider_config(self, provider):

        return self.config.get(
            "providers",
            {}
        ).get(
            provider,
            {}
        )