# Depth-First Search (DFS) in a Grid

## Description
This project implements a **Depth-First Search (DFS)** algorithm in a randomly generated **N x N** grid. The grid consists of **walkable (1) and non-walkable (0) cells**. A **source** and a **goal** node are randomly selected from walkable cells, and DFS is used to explore the grid to find a path.

## Features
- Random **grid generation** with walkable (1) and non-walkable (0) cells.
- Random selection of **source** and **goal** nodes.
- **DFS traversal** to find a path from the source to the goal.
- **Topological order** of traversal is recorded.
- Displays the **grid, path, and traversal order**.

---

## Input
The program does not take manual input; instead, it generates a **random grid** with:
- A grid size between **4x4 and 7x7**.
- Randomly placed **1s (walkable) and 0s (non-walkable)**.
- Random **source (S) and goal (G) locations**.

Example of a randomly generated **5x5 grid**:
```
  1   0   1   1   0  
  S   1   0   1   1  
  0   1   1   1   0  
  1   0   G   1   1  
  1   1   1   0   1  
```

---

## Output
The program displays the **grid**, **source**, **goal**, **DFS path**, and **topological order** of traversal.

### Example Output
```
Grid size: 5x5

  1   0   1   1   0  
  S   1   0   1   1  
  0   1   1   1   0  
  1   0   G   1   1  
  1   1   1   0   1  

Source: (1, 0)
Goal: (3, 2)

DFS Path:
(1, 0) --> (1, 1) --> (2, 1) --> (2, 2) --> (3, 2)

Topological Order of Traversal:
(1, 0) --> (1, 1) --> (2, 1) --> (2, 2) --> (3, 2)
```
If no path exists, the output will state:
```
No path found from Source to Goal.
```

---


