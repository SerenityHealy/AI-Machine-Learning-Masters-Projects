class SoftwareEngineerTrait:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def display(self):
        print(f"Trait: {self.name}")
        print(f"Description: {self.description}")


def main():
    print("Hello, this program describes three personality traits that are "
          "shared among successful software engineers:\n"
          "Adaptability, Continuous Learning, and Productivity.")
    print("\nEach trait plays an important role for software engineers navigating and excelling in the fast-paced "
          "dynamic Tech industry.")

    traits = [
        SoftwareEngineerTrait(
            "Adaptability",
            "A software engineers ability to shift plans and react to issues quickly during a project to remain successful."
        ),
        SoftwareEngineerTrait(
            "Continuous Learning",
            "Software engineers must stay involved in the emerging trends and remain informed on the new technologies."
        ),
        SoftwareEngineerTrait(
            "Productivity",
            "Being a productive software engineer means helping your team and being a reliable source for quality work."
        )
    ]

    print("\nPersonality traits of Successful Software Engineers:")
    for i, trait in enumerate(traits, start=1):
        print(f"\nStep {i}:")
        trait.display()

    # Display the total number of traits (steps)
    print(f"\nNumber of Important Steps (Personality Traits): {len(traits)}")


if __name__ == "__main__":
    main()
