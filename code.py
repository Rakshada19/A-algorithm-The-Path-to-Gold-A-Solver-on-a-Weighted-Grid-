import heapq
import math
import time

# --- 1. Weighted Grid Map (The Game Board) ---
# Each number represents the cost to travel *onto* that tile.
# 1 = Road (Cheap), 5 = Forest (Expensive), 10 = Swamp (Very Expensive)
GRID = [
    [1, 1, 1, 5, 5, 10],
    [1, 5, 1, 1, 5, 10],
    [1, 5, 1, 1, 1, 1],
    [1, 5, 5, 5, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [10, 10, 5, 1, 1, 1]
]

ROWS = len(GRID)
COLS = len(GRID[0])

START = (0, 0)
GOAL = (5, 5)

# Movement directions (Up, Down, Left, Right)
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# --- 2. Heuristic Function (h(n)) ---
def heuristic(a, b):
    """
    Calculates the Manhattan distance between two points (a and b).
    This estimates the remaining cost to the goal.
    """
    (x1, y1) = a
    (x2, y2) = b
    # Formula: |x1 - x2| + |y1 - y2|
    return abs(x1 - x2) + abs(y1 - y2)

# --- 3. The A* Algorithm Implementation ---
def a_star_search(grid, start, goal):
    """
    Finds the cheapest path from start to goal in a weighted grid.
    Returns the path and the total cost.
    """
    # Priority Queue: Stores (f_cost, g_cost, node)
    # f_cost = g_cost + h_cost
    # g_cost = actual cost from start to current node
    priority_queue = [(0, 0, start)]
    
    # g_scores: Stores the minimum known g_cost to reach each node
    g_scores = {start: 0}
    
    # parent_map: Stores the best predecessor for path reconstruction
    parent_map = {start: None}

    start_time = time.time()
    nodes_visited = 0

    while priority_queue:
        # Get the node with the lowest f_cost
        f_cost, g_cost, current_node = heapq.heappop(priority_queue)
        nodes_visited += 1

        if current_node == goal:
            break

        # Explore neighbors
        r, c = current_node
        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            neighbor = (nr, nc)

            # Check bounds
            if 0 <= nr < ROWS and 0 <= nc < COLS:
                # Cost to move to the neighbor is the value of the neighbor tile
                movement_cost = grid[nr][nc]
                
                # tentative_g_score: new cost to reach the neighbor
                new_g_cost = g_scores[current_node] + movement_cost
                
                # If this new path is better (or if the node hasn't been reached yet)
                if neighbor not in g_scores or new_g_cost < g_scores[neighbor]:
                    
                    # Update scores and parent
                    g_scores[neighbor] = new_g_cost
                    parent_map[neighbor] = current_node
                    
                    # Calculate h_cost (heuristic) and f_cost (total estimated cost)
                    h_cost = heuristic(neighbor, goal)
                    f_cost = new_g_cost + h_cost
                    
                    # Add to the priority queue
                    heapq.heappush(priority_queue, (f_cost, new_g_cost, neighbor))
    
    end_time = time.time()
    
    # --- Path Reconstruction ---
    path = []
    current = goal
    total_cost = g_scores.get(goal, 0)
    
    if current in parent_map:
        while current is not None:
            path.append(current)
            current = parent_map.get(current)
        path.reverse()
    
    return path, total_cost, end_time - start_time, nodes_visited

# --- 4. Execution ---

print("--- Weighted Grid Path-to-Gold A* Solver ---")
print(f"Start: {START}, Goal: {GOAL}")
print("Tile Costs (1=Road, 10=Swamp):\n")
for row in GRID:
    print(row)
print("-" * 50)

# Run A*
path, cost, run_time, nodes_visited = a_star_search(GRID, START, GOAL)

# --- 5. Results ---
if path:
    print("✅ Path Found!")
    print(f"Total Minimum Cost (g_score): {cost}")
    print(f"Path Length (Steps): {len(path) - 1}")
    print(f"Nodes Explored (Efficiency): {nodes_visited}")
    print(f"Time Taken: {run_time:.6f} seconds")
    print(f"\nOptimal Path (Coordinates):")
    print(f"{path[:5]} ... {path[-5:]}")
else:
    print("❌ Goal is unreachable.")
