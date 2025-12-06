actors_and_use_cases = {
    "Citizen": [
        {
            "Use Case": "Report Pothole",
            "Description": "Citizens can report potholes based on location and severity."
        },
        {
            "Use Case": "View Repair Status",
            "Description": "Citizens can check the status of potholes that have been reported previously."
        }
    ],
    "System": [
        {
            "Use Case": "Log Pothole Data",
            "Description": "The pothole is assigned an ID number by the system, storing each by its address, size on a scale of 1-10, priority, and location of the curb and district."
        },
        {
            "Use Case": "Generate Work Orders",
            "Description": "Work orders are created by the system for each pothole which include: the location and size, repair crew ID number and amount of people on the crew, equipment required with the status of the hole, and the cost and hours the repair will take."
        },
        {
            "Use Case": "Track Repairs",
            "Description": "A damage file is created for each hole to keep record of each citizens information and cost of damage incurred from pothole damages."
        }
    ],
    "Repair Crew": [
        {
            "Use Case": " Log Repairs",
            "Description": "The repair crew will update the system with the progress of each pothole and once each one is completed."
        },
        {
            "Use Case": "Report Additional Work",
            "Description": "If additional work is required during repairs, the repair crew will notify that there is additional work needed and apply a temporary solution to mitigate the issue. The repair will be rescheduled by the crew to finish the job."
        }
    ]
}


def display_main_menu():
    while True:
        print("\nWelcome to the Pothole Tracking and Repair System! Please choose an option (1-5) to view the use cases for each actor.")
        print("1. View use cases for Citizen")
        print("2. View use cases for System")
        print("3. View use cases for Repair Crew")
        print("4. View a brief description of the diagram")
        print("5. Exit")

        choice = input("Select an option (1-5): ")

        if choice == "1":
            display_actor_use_cases("Citizen")
        elif choice == "2":
            display_actor_use_cases("System")
        elif choice == "3":
            display_actor_use_cases("Repair Crew")
        elif choice == "4":
            display_diagram_description()
        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


def display_actor_use_cases(actor):
    if actor in actors_and_use_cases:
        print(f"\nUse Cases for {actor}:")
        for use_case in actors_and_use_cases[actor]:
            print(f"  - Use Case: {use_case['Use Case']}")
            print(f"    Description: {use_case['Description']}\n")
    else:
        print("Invalid actor selected.")


def display_diagram_description():
    print("\nDiagram Description:")
    print(
        "The Pothole Tracking and Repair System involves three main actors: Citizen, System, and Repair Crew.")
    print(
        "Citizens can report potholes and check their status. The System logs pothole data, generates work orders, and tracks repair progress.")
    print(
        "The Repair Crew executes repairs and logs updates for additional or completed work. The diagram outlines the interaction among these actors, detailing the flow from reporting potholes to completing repairs.")

display_main_menu()
