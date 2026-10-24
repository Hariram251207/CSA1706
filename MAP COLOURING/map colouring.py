"""
================================================================================
ARTIFICIAL INTELLIGENCE: MAP COLOURING PROBLEM (CSP)
================================================================================

ALGORITHM (Backtracking Approach for Graph Colouring):
-----------------------------------------------------
1. Start with the first region/node in the list (index 0).
2. If all regions have been successfully assigned a valid colour, return True.
3. Try assigning each available colour (from 1 to M) to the current region one by one.
4. For each color, check if the assignment is SAFE using the 'is_safe' function:
   - Loop through all other regions on the map.
   - If another region shares a border with our current region AND already has
     the exact same colour, then it is NOT safe. Return False.
5. If the colour choice is SAFE:
   - Assign the colour to the current region.
   - Recursively attempt to color the next region in the list: map_colouring_util(region_index + 1).
   - If the subsequent placements succeed, continue returning True.
   - If moving forward leads to a dead end down the line, BACKTRACK:
     Reset the current region's colour to 0 (uncoloured) and try the next available colour choice.
6. If all available colours have been tested on this region and none work without conflict,
   return False to prompt the previous region to backtrack and change its layout.
================================================================================
"""

import sys

def is_safe(node, graph, colour_assignments, c, num_nodes):
    """Checks if it is safe to assign colour 'c' to the given 'node'."""
    for i in range(num_nodes):
        # If an edge/border exists AND that neighbor has the exact same colour 'c'
        if graph[node][i] == 1 and colour_assignments[i] == c:
            return False
    return True


def map_colouring_util(graph, num_colours, colour_assignments, node, num_nodes):
    """Base backtracking utility function to solve the map colouring layout."""
    # Base Case: If all nodes/regions are assigned a colour, return True
    if node == num_nodes:
        return True

    # Try different colours for the current node
    for c in range(1, num_colours + 1):
        if is_safe(node, graph, colour_assignments, c, num_nodes):
            # Assign the colour
            colour_assignments[node] = c

            # Recur to assign colours to the rest of the nodes
            if map_colouring_util(graph, num_colours, colour_assignments, node + 1, num_nodes):
                return True

            # If assigning colour 'c' doesn't lead to a solution, BACKTRACK
            colour_assignments[node] = 0

    # If no colour can be assigned to this node, return False
    return False


def main():
    print("--- Artificial Intelligence: Map Colouring Solver (CSP) ---")
    
    # 1. RUNTIME INPUTS: Get the regions/states
    raw_regions = input("Enter the names of regions separated by commas (e.g., A, B, C): ").strip()
    if not raw_regions:
        print("Error: You must enter at least one region.")
        sys.exit()
        
    regions = [r.strip() for r in raw_regions.split(",") if r.strip()]
    num_nodes = len(regions)
    
    print(f"\nSuccessfully loaded {num_nodes} regions: {regions}")
    print("Now, let's map out the borders. Enter 1 if they share a border, or 0 if they don't.")
    
    # 2. RUNTIME INPUTS: Build the Adjacency Matrix
    graph = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]
    
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            try:
                border = input(f"Do '{regions[i]}' and '{regions[j]}' share a border? (1 for Yes, 0 for No): ").strip()
                val = int(border)
                if val not in (0, 1):
                    print("Invalid choice! Defaulting to 0 (No border).")
                    val = 0
            except ValueError:
                print("Invalid input! Defaulting to 0 (No border).")
                val = 0
                
            # Symmetric matrix updates since borders work both ways
            graph[i][j] = val
            graph[j][i] = val

    # 3. RUNTIME INPUTS: Get the number of available colours
    try:
        num_colours = int(input("\nEnter the number of available colours (e.g., 2, 3, or 4): "))
    except ValueError:
        print("Error: Input must be a valid whole number.")
        sys.exit()

    if num_colours <= 0:
        print("Error: You must provide at least 1 colour to paint with.")
        sys.exit()

    # Initialize colour array (0 means uncoloured)
    colour_assignments = [0] * num_nodes
    
    # Text mapping labels to make output human-readable
    colour_names = {1: "RED", 2: "GREEN", 3: "BLUE", 4: "YELLOW", 5: "ORANGE"}

    # 4. PROCESS AND SOLVE
    print("\nCalculating valid color configuration...")
    if not map_colouring_util(graph, num_colours, colour_assignments, 0, num_nodes):
        print(f"\n[Result] Failure! A valid solution does not exist using only {num_colours} colour(s).")
    else:
        # 5. OUTPUT THE RESULT
        print("\n=== MAP COLOURING SOLUTION FOUND ===")
        for i in range(num_nodes):
            assigned_id = colour_assignments[i]
            # Use name string if mapped, otherwise display the numeric color ID
            colour_str = colour_names.get(assigned_id, f"Color-{assigned_id}")
            print(f"Region: {regions[i]:<10} ---> Assigned Colour: {colour_str}")
        print("====================================")


if __name__ == "__main__":
    main()
