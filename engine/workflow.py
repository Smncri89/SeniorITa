class WorkflowEngine:


    workflows = {


        "security_fix": [
            "security",
            "developer",
            "test",
            "reviewer",
            "release"
        ],


        "feature_development":[
            "architect",
            "developer",
            "test",
            "reviewer",
            "release"
        ],


        "deployment":[
            "devops",
            "test",
            "release"
        ]

    }



    def get_workflow(self,name):

        return self.workflows.get(
            name,
            []
        )
    