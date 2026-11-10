
"""
Experiment 3: Water Jug Problem using BFS
Author: Anushka Sharma
Roll No: IC-2K23-12
"""

from collections import deque


def get_next_states(state, capacity_a, capacity_b):
    """Generate all possible next states."""

    a, b = state

    # Amount of water that can be poured
    pour_a_b = min(a, capacity_b - b)
    pour_b_a = min(b, capacity_a - a)

    return [
        ("Fill Jug A", (capacity_a, b)),
        ("Fill Jug B", (a, capacity_b)),
        ("Empty Jug A", (0, b)),
        ("Empty Jug B", (a, 0)),
        ("Pour A to B", (a - pour_a_b, b + pour_a_b)),
        ("Pour B to A", (a + pour_b_a, b - pour_b_a))
    ]


def water_jug_bfs(capacity_a, capacity_b, target):
    """Solve the Water Jug Problem using BFS."""

    initial_state = (0, 0)

    queue = deque([initial_state])

    visited = {initial_state}

    parent = {initial_state: None}
    actions = {}

    goal_state = None

    while queue:

        current = queue.popleft()

        a, b = current

        # Check goal condition
        if a == target or b == target:
            goal_state = current
            break

        # Generate next states
        for action, next_state in get_next_states(
            current, capacity_a, capacity_b
        ):

            if next_state not in visited:

                visited.add(next_state)
                parent[next_state] = current
                actions[next_state] = action

                queue.append(next_state)

    if goal_state is None:
        return None

    # Reconstruct solution path
    path = []
    current = goal_state

    while current is not None:

        path.append((current, actions.get(current)))
        current = parent[current]

    path.reverse()

    return path


def main():

    capacity_a = 4
    capacity_b = 3
    target = 2

    print("WATER JUG PROBLEM USING BFS")
    print("-" * 40)

    print("Jug A Capacity:", capacity_a, "Litres")
    print("Jug B Capacity:", capacity_b, "Litres")
    print("Target Amount:", target, "Litres")

    solution = water_jug_bfs(
        capacity_a, capacity_b, target
    )

    if solution is None:
        print("\nNo solution exists.")
        return

    print("\nSolution Found!")
    print("\nStep-by-step solution:")

    for step, (state, action) in enumerate(solution):

        if action:
            print(
                f"Step {step}: {action} -> {state}"
            )
        else:
            print(f"Step {step}: Initial State -> {state}")

    print("\nGoal Reached:", solution[-1][0])


if __name__ == "__main__":
    main()
