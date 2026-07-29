from dataclasses import dataclass
from typing import List


@dataclass
class Agent:
    name: str
    role: str
    priority: str
    responsibilities: List[str]


@dataclass
class Workflow:
    name: str
    agents: List[Agent]


@dataclass
class ExecutionContext:
    project: str
    workflow: Workflow