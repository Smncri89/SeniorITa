import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))


from engine.agent_loader import AgentLoader


loader = AgentLoader()

agents = loader.load_agents()


for agent in agents:
    print(
        agent.name,
        "-",
        agent.role
    )