from simpleai.search import SearchProblem, greedy

def get_motor_input():
    print("Enter which motors are working (Y/N):")
    motor_a = input("Motor A (moves +1 floor): ").strip().upper() == 'Y'
    motor_b = input("Motor B (moves +2 floors): ").strip().upper() == 'Y'
    motor_c = input("Motor C (moves -1 floor): ").strip().upper() == 'Y'
    return {
        "A": motor_a,
        "B": motor_b,
        "C": motor_c
    }

def get_goal_floor():
    while True:
        try:
            goal = int(input("Enter the goal floor (0 to 4): "))
            if 0 <= goal <= 4:
                return goal
            else:
                print("Floor must be between 0 and 4.")
        except ValueError:
            print("Please enter a number.")

class ElevatorRescueProblem(SearchProblem):
    def __init__(self, goal_floor, working_motors):
        self.goal_floor = goal_floor
        self.working_motors = working_motors
        super().__init__(initial_state=0)

    def actions(self, state):
        actions = []
        if self.working_motors["A"] and state + 1 <= 4:
            actions.append("UP_1")
        if self.working_motors["B"] and state + 2 <= 4:
            actions.append("UP_2")
        if self.working_motors["C"] and state - 1 >= 0:
            actions.append("DOWN_1")
        return actions

    def result(self, state, action):
        if action == "UP_1":
            return state + 1
        elif action == "UP_2":
            return state + 2
        elif action == "DOWN_1":
            return state - 1

    def is_goal(self, state):
        return state == self.goal_floor

    def heuristic(self, state):
        return abs(self.goal_floor - state)

def main():
    goal_floor = get_goal_floor()
    working_motors = get_motor_input()

    problem = ElevatorRescueProblem(goal_floor, working_motors)
    result = greedy(problem)

    print("\nPath to goal floor:")
    for action, state in result.path():
        print(f"Floor {state} ({action})")

if __name__ == "__main__":
    main()
