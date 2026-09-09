# Water Jug Problem

A C++ implementation of the classic **Water Jug Problem** using **Breadth-First Search (BFS)**.

## Problem Statement

You are given two jugs with capacities `4L` and `3L`. Neither jug has measurement markings. Using only these two jugs, measure exactly `2L` of water.

### Allowed Operations

1. Fill a jug completely.
2. Empty a jug completely.
3. Pour water from one jug into the other until either the source is empty or the destination is full.

## Algorithm

The problem is solved using **BFS**, where each state represents the amount of water in both jugs.

For example:

```text
(a, b)
```

Here:

* `a` = water in Jug A
* `b` = water in Jug B

The initial state is:

```text
(0, 0)
```

The algorithm explores all possible states until one jug contains the target amount.

## Example

### Input

```text
Jug A Capacity = 4L
Jug B Capacity = 3L
Target = 2L
```

### Output

```text
Target reached!
```

## How to Run

### 1. Save the code

Save the C++ program as:

```text
water_jug.cpp
```

### 2. Compile

```bash
g++ water_jug.cpp -o water_jug
```

### 3. Run

```bash
./water_jug
```

## Complexity

Let `m` and `n` be the capacities of the two jugs.

* **Time Complexity:** `O(m × n)`
* **Space Complexity:** `O(m × n)`

Each possible state is visited at most once.

## Requirements

* C++ compiler
* Basic knowledge of BFS
* Basic knowledge of queues and sets

## Learning Outcomes

* Understand the Water Jug Problem.
* Learn how BFS explores states.
* Understand state-space search.
* Practice using `queue` and `set` in C++.

## Author

Anushka Sharma
