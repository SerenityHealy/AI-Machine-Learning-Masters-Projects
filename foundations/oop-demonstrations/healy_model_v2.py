class HealyModel:
    def __init__(self):
        self.phases = {
            "Communication": {},
            "Planning": {},
            "Modeling": {},
            "Construction": {},
            "Deployment": {}
        }

    def input_phase_details(self):
        print("\n=== Healy Model: Software Project Organizer ===")
        print("Follow the guided questions with detailed answers to organize your project workflow.\n")

        print("\nCommunication Phase:")
        self.phases["Communication"]["Stakeholders"] = input(
            "Who are the stakeholders involved, and how will you gather requirements from them? ")
        self.phases["Communication"]["Initial Challenges"] = input(
            "What feedback or changes were identified from stakeholders before initial design? ")
        self.phases["Communication"]["Goal of the Project"] = input(
            "What is the main goal of the project? ")

        print("\nPlanning Phase:")
        self.phases["Planning"]["Resource Needs"] = input(
            "What resources are needed for the project? (employees, budget, software tools) ")
        self.phases["Planning"]["Timeline"] = input(
            "What is the expected timeline for each phase and total? ")
        self.phases["Planning"]["Risk Management"] = input(
            "What are the potential risks, and how will you address them? ")

        print("\nModeling Phase:")
        self.phases["Modeling"]["Analysis Approval Plan"] = input(
            "What is the approval process for software project requirements? ")
        self.phases["Modeling"]["Software Design Tools"] = input(
            "What specific tools will be used to design the software? ")
        self.phases["Modeling"]["Early Testing"] = input(
            "How will the software tests be conducted and how will you gather feedback from testing team? ")

        print("\nConstruction Phase:")
        self.phases["Construction"]["Development Tasks"] = input(
            "What practices or coding standards will be used to develop the software? ")
        self.phases["Construction"]["Testing Plan"] = input(
            "How will you utilize the testing team to gather feedback and make changes to the software? ")
        self.phases["Construction"]["Change Management"] = input(
            "How will you handle changes or bugs discovered during testing? ")

        print("\nDeployment Phase:")
        self.phases["Deployment"]["Rollout Strategy"] = input(
            "How will the software be implemented and rolled out to the users? Gradually? ")
        self.phases["Deployment"]["Support Plan"] = input(
            "What resources will be used to support the users post deployment? ")
        self.phases["Deployment"]["Feedback Process"] = input(
            "How will you collect and act on user feedback after deployment? ")

    def display_model_summary(self):
        print("\n=== Project Summary: Healy Model ===")
        for phase, details in self.phases.items():
            print(f"\n{phase} Phase:")
            for key, value in details.items():
                print(f"  - {key}: {value}")


if __name__ == "__main__":
    model = HealyModel()
    model.input_phase_details()
    model.display_model_summary()
