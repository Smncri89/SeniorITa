# -*- coding: utf-8 -*-

from pathlib import Path


class PromptLoader:

    @staticmethod
    def load(path):

        file = Path(path)

        if not file.exists():
            raise FileNotFoundError(
                f"Prompt non trovato: {path}"
            )

        return file.read_text(
            encoding="utf-8"
        )