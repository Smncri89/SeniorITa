# -*- coding: utf-8 -*-

from engine.providers.provider_factory import ProviderFactory
from engine.model_router import ModelRouter


class AgentExecutor:


    def __init__(self):

        self.router = ModelRouter()



    def execute(
        self,
        agent,
        request
    ):


        # Selezione automatica modello

        routing = self.router.select_model(
            request,
            agent
        )


        provider_name = routing["provider"]

        model = routing["model"]



        provider = ProviderFactory.create(
            provider_name,
            model
        )



        prompt = f"""

Rispondi sempre in lingua italiana.

Sei un agente AI enterprise.

Ruolo agente:

{agent['role']}


Nome agente:

{agent['name']}


Capacità:

{agent['capabilities']}


Richiesta utente:

{request}


Modello utilizzato:

{model}


Motivo scelta:

{routing['reason']}


Fornisci una risposta professionale,
tecnica e strutturata.

Usa esempi pratici quando utili.


"""



        response = provider.generate(
            prompt
        )


        return {

            "agent": agent["name"],

            "provider": provider_name,

            "model": model,

            "model_reason": routing["reason"],

            "response": response

        }