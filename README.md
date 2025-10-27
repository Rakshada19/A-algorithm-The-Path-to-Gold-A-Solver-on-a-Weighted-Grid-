The A* algorithm achieves optimal pathfinding by combining two components:

1. Cost-So-Far ($g(n)$): The actual accumulated cost from the starting node to the current node. This is crucial in a weighted grid.
2. Heuristic ($h(n)$): The estimated cost from the current node to the goal. We use the Manhattan Distance for this estimate.
  
A* prioritizes nodes based on the total estimated cost: $\mathbf{f(n) = g(n) + h(n)}$.
The "game" environment is a 6x6 grid where each number represents the cost incurred when moving onto that tile. 
The objective is to find the path from Start (0, 0) to Goal (5, 5) that minimizes the total accumulated cost.

Visual Representation of the Grid:
[1, 1, 1, 5, 5, 10]  (Start at 1)
[1, 5, 1, 1, 5, 10]
[1, 5, 1, 1, 1, 1]
[1, 5, 5, 5, 1, 1]
[1, 1, 1, 1, 1, 1]
[10, 10, 5, 1, 1, 1]  (Goal at 1)
