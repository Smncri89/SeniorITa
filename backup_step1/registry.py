from engine.agent_loader import AgentLoader


class AgentRegistry:

    def __init__(self):
        self.loader = AgentLoader()
        self.agents = self.loader.load_agents()["agents"]


    def list_agents(self):
        return self.agents


    def get_agent(self, name):

        for agent in self.agents:
            if agent["name"] == name:
                return agent

        return None


    def find_by_capability(self, capability):

        results = []

        for agent in self.agents:
            if capability in agent.get("capabilities", []):
                results.append(agent)

        return results
    