from pathlib import Path
import yaml


class AgentLoader:

    def __init__(self, agents_file=".github/agents.yaml"):
        self.agents_file = Path(agents_file)


    def load_agents(self):

        if not self.agents_file.exists():
            raise FileNotFoundError(
                f"Agent registry not found: {self.agents_file}"
            )

        with open(
            self.agents_file,
            "r",
            encoding="utf-8"
        ) as file:
            data = yaml.safe_load(file)

        return data


    def get_agent(self, name):

        agents = self.load_agents()

        for agent in agents.get("agents", []):
            if agent.get("name") == name:
                return agent

        return None