# Elevator Rescue Problem

An AI search problem solver using greedy best-first search to navigate a broken elevator with partially functioning motors.

## Overview

This project implements a greedy search algorithm to solve the "broken elevator" problem. Given a 5-floor building (floors 0-4) with three motors that may be broken, the algorithm finds a path from floor 0 to any goal floor.

## Problem Description

**Scenario**: Elevator has three motors:
- **Motor A**: Moves +1 floor (up one floor)
- **Motor B**: Moves +2 floors (up two floors)
- **Motor C**: Moves -1 floor (down one floor)

**Challenge**: Some motors may be broken. Find a path to the goal floor using only working motors.

## Features

- **Interactive Configuration**: User specifies which motors work
- **Greedy Best-First Search**: Uses heuristic to guide search
- **Dynamic Action Generation**: Only considers valid moves
- **Path Display**: Shows complete solution path
- **Boundary Checking**: Ensures elevator stays in 0-4 range

## Installation

```bash
# Install simpleai library
pip install simpleai
```

## Usage

```bash
python elevator_rescue.py
```

### Example Session

```
Enter the goal floor (0 to 4): 3

Enter which motors are working (Y/N):
Motor A (moves +1 floor): Y
Motor B (moves +2 floors): N
Motor C (moves -1 floor): Y

Path to goal floor:
Floor 0 (None)
Floor 1 (UP_1)
Floor 2 (UP_1)
Floor 3 (UP_1)
```

## How It Works

### Search Algorithm

Uses **Greedy Best-First Search**:
1. Start at floor 0
2. Generate available actions (only working motors)
3. Select action with lowest heuristic value
4. Repeat until goal floor reached

### Heuristic Function

```python
h(state) = |goal_floor - current_floor|
```

Estimates remaining distance to goal (Manhattan distance).

### State Space

- **States**: Floor numbers {0, 1, 2, 3, 4}
- **Actions**: {UP_1, UP_2, DOWN_1} (if motor works)
- **Initial State**: Floor 0
- **Goal Test**: current_floor == goal_floor

## Code Structure

### Class: ElevatorRescueProblem

Inherits from `SearchProblem` (simpleai)

**Methods**:
- `__init__()`: Initialize goal and working motors
- `actions(state)`: Generate valid moves from current floor
- `result(state, action)`: Compute new floor after action
- `is_goal(state)`: Check if at goal floor
- `heuristic(state)`: Estimate distance to goal

### Helper Functions

- `get_motor_input()`: Interactive motor configuration
- `get_goal_floor()`: Validate and get goal floor (0-4)
- `main()`: Orchestrate problem setup and solving

## Example Scenarios

### Scenario 1: All Motors Working

```
Goal: Floor 4
Motors: A=Y, B=Y, C=Y

Optimal Path:
Floor 0 → Floor 2 (UP_2) → Floor 4 (UP_2)
```

### Scenario 2: Only Motor A Working

```
Goal: Floor 3
Motors: A=Y, B=N, C=N

Path:
Floor 0 → Floor 1 (UP_1) → Floor 2 (UP_1) → Floor 3 (UP_1)
```

### Scenario 3: No Upward Motors

```
Goal: Floor 2
Motors: A=N, B=N, C=Y

Result: No solution (cannot go up)
```

## Greedy vs Other Search Algorithms

| Algorithm | Completeness | Optimality | Time Complexity |
|-----------|--------------|------------|-----------------|
| Greedy | No | No | O(b^m) |
| A* | Yes | Yes | O(b^d) |
| Breadth-First | Yes | Yes | O(b^d) |

**Greedy Advantage**: Fast, low memory
**Greedy Disadvantage**: May not find shortest path, may not find solution

## Technical Details

**Language**: Python 3
**Library**: simpleai (AI search algorithms)
**Search Type**: Informed search (uses heuristic)
**State Representation**: Integer (floor number)
**Action Representation**: String (UP_1, UP_2, DOWN_1)

## Possible Enhancements

1. **Try A* Search**: Optimal pathfinding
   ```python
   from simpleai.search import astar
   result = astar(problem)
   ```

2. **Add Motor Costs**: Different energy costs per motor
   ```python
   def cost(self, state, action):
       return {"UP_1": 1, "UP_2": 3, "DOWN_1": 1}[action]
   ```

3. **More Floors**: Extend beyond 5 floors

4. **Broken Floor Constraints**: Some floors inaccessible

5. **Multiple Elevators**: Coordinate between elevators

## Learning Outcomes

- AI search problem formulation
- State space representation
- Heuristic function design
- Greedy best-first search algorithm
- Search problem constraints
- simpleai library usage

## Related Concepts

- **Informed Search**: Uses domain knowledge (heuristic)
- **Graph Search**: Avoiding repeated states
- **Admissible Heuristic**: Never overestimates (for A*)
- **Search Space**: All possible states and transitions
