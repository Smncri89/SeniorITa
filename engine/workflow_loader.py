# -*- coding: utf-8 -*-

import yaml


class WorkflowLoader:

    @staticmethod
    def load(path):

        with open(
            path,
            encoding="utf-8"
        ) as file:

            return yaml.safe_load(file)