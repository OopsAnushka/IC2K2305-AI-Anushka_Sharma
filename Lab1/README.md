
# Lab 1 - AI Environment Setup and Problem Solving

**Student Name:** Anushka Sharma

**Roll Number:** IC-2K23-12

**Course:** IC-709D - Artificial Intelligence Lab

---

## Experiment 1: AI Environment Setup

### Aim
To set up and verify the Python development environment
required for Artificial Intelligence experiments.

### Tools Used
- Python
- VS Code
- Jupyter Notebook
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- PyTorch

### Algorithm
1. Import Python system modules.
2. Display Python version.
3. Identify operating system.
4. Check the availability of AI libraries.
5. Display library installation status.

### Result
The Python environment was successfully checked
and the availability of AI libraries was verified.

### Output
![Environment Setup](outputs/experiment1_output.png)

---

## Experiment 2: Production Rule System

### Aim
To implement a production rule system using IF-THEN
rules for intelligent decision-making.

### Theory
A production system consists of production rules,
working memory and a control strategy.

### Algorithm
1. Initialize working memory with facts.
2. Define production rules.
3. Check the conditions of each rule.
4. Execute the matching rule.
5. Update working memory.
6. Repeat until no rule can be applied.
7. Display the final facts.

### Result
The system successfully applied IF-THEN rules
to control a fan and open a window based on temperature.

### Output
![Production System](outputs/experiment2_output.png)

---

## Experiment 3: Water Jug Problem using BFS

### Aim
To solve the Water Jug Problem using Breadth First Search.

### Problem Statement
There are two jugs with capacities of 4 litres and
3 litres. The objective is to obtain exactly 2 litres
of water in either jug.

### Algorithm
1. Start with both jugs empty.
2. Insert the initial state into a queue.
3. Remove the first state from the queue.
4. Generate all possible next states.
5. Check whether the goal state is reached.
6. Add unvisited states to the queue.
7. Repeat until the goal is found.
8. Display the solution path.

### Result
The Water Jug Problem was successfully solved.
The final state obtained was (4, 2).

### Performance Analysis

- Search Algorithm: Breadth First Search
- Time Complexity: O(V + E)
- Space Complexity: O(V)
- V: Number of reachable states
- E: Number of transitions between states

### Output
![Water Jug Output](outputs/experiment3_output.png)

---

## Learning Outcomes

1. Learned how to configure a Python AI environment.
2. Understood production systems and IF-THEN rules.
3. Learned working memory and rule-based reasoning.
4. Understood state space representation.
5. Implemented Breadth First Search.
6. Learned how to solve the Water Jug Problem.

---

## Conclusion

All three experiments were successfully implemented
using Python. The experiments provided practical
understanding of AI environment setup, production
systems, state space representation and BFS.
