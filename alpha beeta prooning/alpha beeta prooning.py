"""
================================================================================
ARTIFICIAL INTELLIGENCE: ALPHA-BETA PRUNING WITH TREE VISUALIZATION
================================================================================

ALGORITHM:
----------
1. Collect leaf node inputs from the user.
2. Build the entire game tree level-by-level from the bottom up by simulating 
   the choices of Maximizer and Minimizer layers.
3. Print a structural visual diagram to the console using indentation layers.
4. Execute Alpha-Beta Depth-First Search Pruning over the parsed array.
================================================================================
"""

import math
import sys

# Global counter to track how many leaf nodes we actually looked at
evaluated_leaves_count = 0

def build_full_tree(leaves, target_depth):
    """
    Builds a full list representing all nodes of the binary tree.
    Index 0 is the root, indices 1-2 are depth 1, etc.
    """
    tree_size = (2 ** (target_depth + 1)) - 1
    tree = [0] * tree_size
    
    # Place leaves at the bottom of the tree array
    leaf_start_idx = (2 ** target_depth) - 1
    for i in range(len(leaves)):
        tree[leaf_start_idx + i] = leaves[i]
        
    # Calculate internal node values from the bottom up to show true game values
    for d in range(target_depth - 1, -1, -1):
        start_idx = (2 ** d) - 1
        num_nodes = 2 ** d
        is_max_layer = (d % 2 == 0) # Level 0 is Max, Level 1 is Min, etc.
        
        for i in range(num_nodes):
            curr_idx = start_idx + i
            left_child = curr_idx * 2 + 1
            right_child = curr_idx * 2 + 2
            
            if is_max_layer:
                tree[curr_idx] = max(tree[left_child], tree[right_child])
            else:
                tree[curr_idx] = min(tree[left_child], tree[right_child])
    return tree


def print_tree_structure(tree, idx, depth, target_depth):
    """Recursively prints the binary tree with clean structural indentation."""
    if depth > target_depth:
        return

    # Determine what kind of player layer this node belongs to
    if depth == target_depth:
        layer_type = "[Leaf]"
    elif depth % 2 == 0:
        layer_type = "[MAX]"
    else:
        layer_type = "[MIN]"

    # Right child first (so visual tree reads top-to-bottom/right-to-left accurately)
    right_child = idx * 2 + 2
    if right_child < len(tree):
        print_tree_structure(tree, right_child, depth + 1, target_depth)

    # Print the current node with structural spacing matching its depth
    indentation = "    " * depth
    print(f"{indentation}---> {layer_type} Value: {tree[idx]}")

    # Left child
    left_child = idx * 2 + 1
    if left_child < len(tree):
        print_tree_structure(tree, left_child, depth + 1, target_depth)


def alpha_beta_pruning(depth, node_index, is_max, leaves, alpha, beta, target_depth):
    """Evaluates the tree while pruning subtrees when alpha >= beta."""
    global evaluated_leaves_count

    # Base Case: Reached a leaf node
    if depth == target_depth:
        evaluated_leaves_count += 1
        return leaves[node_index]

    if is_max:
        max_eval = -math.inf
        for i in range(2):
            child_index = node_index * 2 + i
            eval_score = alpha_beta_pruning(depth + 1, child_index, False, leaves, alpha, beta, target_depth)
            max_eval = max(max_eval, eval_score)
            alpha = max(alpha, max_eval)
            
            if alpha >= beta:
                print(f"  [Pruned] MAX layer cut off remaining branches at depth {depth} (Alpha:{alpha} >= Beta:{beta})")
                break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(2):
            child_index = node_index * 2 + i
            eval_score = alpha_beta_pruning(depth + 1, child_index, True, leaves, alpha, beta, target_depth)
            min_eval = min(min_eval, eval_score)
            beta = min(beta, min_eval)
            
            if alpha >= beta:
                print(f"  [Pruned] MIN layer cut off remaining branches at depth {depth} (Alpha:{alpha} >= Beta:{beta})")
                break
        return min_eval


def main():
    global evaluated_leaves_count
    print("--- AI: Alpha-Beta Pruning with Structural Tree Mapping ---")
    
    # 1. RUNTIME INPUT
    print("Provide game outcomes (leaf scores) separated by commas.")
    print("Count MUST be a power of 2 (e.g., 4, 8, 16).")
    raw_input = input("Enter values (e.g., 3, 5, 2, 9): ").strip()
    
    if not raw_input:
        print("Error: Input cannot be empty.")
        sys.exit()

    try:
        leaves = [int(x.strip()) for x in raw_input.split(",") if x.strip()]
    except ValueError:
        print("Error: All values must be clean integers.")
        sys.exit()

    num_leaves = len(leaves)
    if num_leaves < 2 or (num_leaves & (num_leaves - 1)) != 0:
        print(f"Error: You entered {num_leaves} items. It must be a power of 2 (4, 8, 16...) to build a valid binary tree.")
        sys.exit()

    target_depth = int(math.log2(num_leaves))
    
    # 2. GENERATE AND PRINT TREE STRUCTURE
    print("\n================ VISUAL GAME TREE ================")
    full_tree = build_full_tree(leaves, target_depth)
    print_tree_structure(full_tree, 0, 0, target_depth)
    print("==================================================")
    
    # 3. COMPUTE EVALUATION WITH PRUNING
    print("\nRunning Alpha-Beta Pruning Evaluation...")
    optimal_score = alpha_beta_pruning(0, 0, True, leaves, -math.inf, math.inf, target_depth)
    
    # 4. FINAL PERFORMANCE REPORT
    print("\n=== SEARCH SUMMARY ===")
    print(f"Optimal Result from Root : {optimal_score}")
    print(f"Total Leaves in Game     : {num_leaves}")
    print(f"Leaves Inspected         : {evaluated_leaves_count}")
    print(f"Leaves Pruned / Skipped  : {num_leaves - evaluated_leaves_count}")
    print("=======================")

if __name__ == "__main__":
    main()
