# DFS and BFS Graph Traversal

This project contains C++ implementations of **Depth First Search (DFS)** and **Breadth First Search (BFS)** using an adjacency list.

## 📌 Algorithms

### 1. Depth First Search (DFS)

DFS explores a graph by going as deep as possible before backtracking.

**Data structure used:** Recursion / Stack

**Time Complexity:** O(V + E)

**Space Complexity:** O(V)

### 2. Breadth First Search (BFS)

BFS explores a graph level by level, visiting all neighboring vertices before moving to the next level.

**Data structure used:** Queue

**Time Complexity:** O(V + E)

**Space Complexity:** O(V)

Where:

* **V** = Number of vertices
* **E** = Number of edges

## 📂 Files

```text
DFS-BFS/
│
├── dfs.cpp
├── bfs.cpp
└── README.md
```

## ⚙️ Requirements

* C++ compiler
* VS Code / Code::Blocks / any C++ IDE
* Basic knowledge of graphs

## 🚀 How to Run

### Compile DFS

```bash
g++ dfs.cpp -o dfs
```

### Run DFS

```bash
./dfs
```

### Compile BFS

```bash
g++ bfs.cpp -o bfs
```

### Run BFS

```bash
./bfs
```

> On Windows, use `dfs.exe` and `bfs.exe` to run the compiled programs.

## 🧪 Sample Input

```text
Enter number of vertices and edges: 5 5
Enter edges:
0 1
0 2
1 3
1 4
2 4
Enter starting vertex: 0
```

## 📤 Sample Output

### DFS

```text
DFS Traversal: 0 1 3 4 2
```

### BFS

```text
BFS Traversal: 0 1 2 3 4
```

> Traversal order may vary depending on the order of edges in the adjacency list.

## 🔍 Difference Between DFS and BFS

| Feature                           | DFS                           | BFS                                  |
| --------------------------------- | ----------------------------- | ------------------------------------ |
| Full Form                         | Depth First Search            | Breadth First Search                 |
| Approach                          | Goes deep first               | Goes level by level                  |
| Data Structure                    | Stack / Recursion             | Queue                                |
| Shortest Path in Unweighted Graph | Not guaranteed                | Guaranteed                           |
| Memory                            | O(V)                          | O(V)                                 |
| Common Applications               | Maze solving, cycle detection | Shortest path, level-order traversal |

## 📝 Notes

* The programs use **0-based vertex numbering**.
* The graph is **undirected** by default.
* To create a directed graph, remove the second `push_back()` statement.
* The starting vertex must be between `0` and `V - 1`.
* For disconnected graphs, run DFS/BFS from every unvisited vertex to visit the entire graph.

## 👩‍💻 Author

**Anushka Sharma**


