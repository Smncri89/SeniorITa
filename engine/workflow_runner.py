from engine.agent_executor import AgentExecutor
from engine.registry import AgentRegistry


class WorkflowRunner:

    def __init__(self):

        self.registry = AgentRegistry()
        self.executor = AgentExecutor()


    def run(self, workflow, request):

        context = {}

        execution_log = []


        for agent_name in workflow:

            agent = self.registry.get_agent(agent_name)


            if not agent:
                execution_log.append(
                    {
                        "agent": agent_name,
                        "status": "missing"
                    }
                )

                continue


            result = self.executor.execute(
                agent,
                request
            )


            context[agent_name] = result


            execution_log.append(
                {
                    "agent": agent_name,
                    "status": "completed",
                    "instructions_loaded": result.get(
                        "instructions_loaded",
                        False
                    )
                }
            )


        return {

            "request": request,

            "workflow_execution": execution_log,

            "context": context,

            "final_status": "completed"

        }