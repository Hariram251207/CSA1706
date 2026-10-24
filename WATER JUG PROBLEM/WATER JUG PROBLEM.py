"""
================================================================================
ARTIFICIAL INTELLIGENCE: WATER JUG PROBLEM SOLVER (BFS)
================================================================================

ALGORITHM (Breadth-First Search):
---------------------------------
1. Initialize a Queue to store the states to explore. Each state is represented 
   as a tuple (j1, j2) where 'j1' is current water in Jug 1 and 'j2' is in Jug 2.
2. Initialize a Dictionary or Set called 'visited' to keep track of states we've 
   already checked to prevent infinite loops.
3. Track the steps taken by storing the path history inside the queue along with the state.
4. While the queue is not empty:
   - Pop the front state.
   - If either j1 or j2 matches the Target Volume, a solution is found! Print the path.
   - Otherwise, generate all possible next legal moves from the current state:
     a. Fill Jug 1 completely -> (Jug1_Capacity, j2)
     b. Fill Jug 2 completely -> (j1, Jug2_Capacity)
     c. Empty Jug 1 completely -> (0, j2)
     d. Empty Jug 2 completely -> (j1, 0)
     e. Pour from Jug 1 to Jug 2 until Jug 2 is full or Jug 1 is empty.
     f. Pour from Jug 2 to Jug 1 until Jug 1 is full or Jug 2 is empty.
   - For each generated move, if it hasn't been 'visited' yet, add it to the queue
     and mark it as visited.
5. If the queue becomes empty and the target wasn't reached, no solution exists.
================================================================================
"""

from collections import deque
import sys

def solve_water_jug(amt1, amt2, target):
    """
    Finds the shortest path to solve the water jug problem using BFS.
    amt1: Capacity of Jug 1
    amt2: Capacity of Jug 2
    target: The desired amount of water
    """
    # Queue stores: ((current_jug1, current_jug2), [path_history_list])
    # Starting state: both jugs are empty (0, 0)
    queue = deque([((0, 0), [(0, 0)])])
    
    # Set to keep track of visited configurations
    visited = set()
    visited.add((0, 0))
    
    while queue:
        (j1, j2), path = queue.popleft()
        
        # Goal Check: If either jug hits the target value, return the successful path
        if j1 == target or j2 == target:
            return path
            
        # Generate all 6 possible next moves rules:
        moves = [
            (amt1, j2),  # 1. Fill Jug 1
            (j1, amt2),  # 2. Fill Jug 2
            (0, j2),     # 3. Empty Jug 1
            (j1, 0),     # 4. Empty Jug 2
            
            # 5. Pour Jug 1 -> Jug 2
            (j1 - min(j1, amt2 - j2), j2 + min(j1, amt2 - j2)),
            
            # 6. Pour Jug 2 -> Jug 1
            (j1 + min(j2, amt1 - j1), j2 - min(j2, amt1 - j1))
        ]
        
        for move in moves:
            if move not in visited:
                visited.add(move)
                # Append the new state to the historical path list
                new_path = list(path)
                new_path.append(move)
                queue.append((move, new_path))
                
    return None  # Return None if no solution path can be mapped mathematically


def main():
    print("--- Artificial Intelligence: Water Jug Solver ---")
    
    # 1. RUNTIME INPUTS & CONSTRAINTS CHECK
    try:
        amt1 = int(input("Enter capacity of Jug 1 (e.g., 4): "))
        amt2 = int(input("Enter capacity of Jug 2 (e.g., 3): "))
        target = int(input("Enter the Target volume needed (e.g., 2): "))
    except ValueError:
        print("Error: All inputs must be valid integers.")
        sys.exit()

    if amt1 <= 0 or amt2 <= 0 or target < 0:
        print("Error: Capacities must be positive integers.")
        sys.exit()
        
    if target > max(amt1, amt2):
        print(f"Error: Target volume ({target}L) cannot be larger than your biggest jug ({max(amt1, amt2)}L).")
        sys.exit()

    # Mathematical rule: Target must be a multiple of the Greatest Common Divisor (GCD) of both jugs
    def get_gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    if target % get_gcd(amt1, amt2) != 0:
        print(f"\n[Result] Mathematically impossible! No solution exists.")
        print(f"The target must be a multiple of the GCD of both jugs (GCD is {get_gcd(amt1, amt2)}).")
        sys.exit()

    # 2. PROCESS AND SOLVE
    print(f"\nSearching for fastest path to get {target}L using a {amt1}L and {amt2}L jug...")
    result_path = solve_water_jug(amt1, amt2, target)
    
    # 3. VISUAL DISPLAY OF PATH OUTPUT
    if result_path:
        print("\n=== SOLUTION PATH FOUND ===")
        print(f"Step {'':<4} | Jug 1 ({amt1}L) | Jug 2 ({amt2}L)")
        print("-" * 38)
        for i, (j1, j2) in enumerate(result_path):
            print(f"Step {i:<4} | {j1:<10} | {j2:<10}")
        print("===========================")
        print("Success! Target achieved.")
    else:
        print("\n[Result] No valid sequence of steps could find this target.")

if __name__ == "__main__":
    main()