def has_cycle(adj_list):
    if not adj_list:
        return False
    
    # Handle single node case
    if len(adj_list) == 1:
        return len(adj_list[0]) > 0
    
    visited = set()
    rec_stack = set()  # Tracks current DFS path
    
    def dfs(node):
        visited.add(node)
        rec_stack.add(node)
        
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True
        
        rec_stack.remove(node)
        return False
    
    # Check all components
    for node in range(len(adj_list)):
        if dfs(node):
            return True
    return False

# Graph: 0 → 1 → 2 → 0 (cycle)
cycle_3_nodes = {
    0: [1],    # Node 0 points to node 1
    1: [2],    # Node 1 points to node 2  
    2: [0]     # Node 2 points to node 0 (creates cycle)
}
# Expected: HAS CYCLE

# Graph: 0 → 1 → 2 (no cycle)
no_cycle_3_nodes = {
    0: [1],    # Node 0 points to node 1
    1: [2],    # Node 1 points to node 2
    2: []      # Node 2 points to nothing
}
# Expected: NO CYCLE

# Graph: 0 → 0 (self cycle)
self_loop = {
    0: [0]     # Node 0 points to itself
}
# Expected: HAS CYCLE

# Graph: 0 → 1, 2 → 3 → 2 (cycle in component 2-3)
mixed_components = {
    0: [1],    # Node 0 → 1
    1: [],     # Node 1 → nothing
    2: [3],    # Node 2 → 3
    3: [2]     # Node 3 → 2 (creates cycle)
}
# Expected: HAS CYCLE

# Additional test cases:

# Tree structure (No cycle)
tree_structure = {
    0: [1, 2],   # Node 0 → 1, 2
    1: [3],      # Node 1 → 3
    2: [],       # Node 2 → nothing
    3: []        # Node 3 → nothing
}
# Expected: NO CYCLE

# More complex cycle
complex_cycle = {
    0: [1, 3],   # Node 0 → 1, 3
    1: [2],      # Node 1 → 2
    2: [4],      # Node 2 → 4
    3: [2],      # Node 3 → 2
    4: [1]       # Node 4 → 1 (creates cycle: 1→2→4→1)
}
# Expected: HAS CYCLE

# Empty graph (single isolated node)
empty_graph = {
    0: []        # Node 0 points to nothing
}
# Expected: NO CYCLE

# Multiple disconnected components, no cycles
disconnected_no_cycle = {
    0: [1],      # Component 1: 0 → 1
    1: [],
    2: [3],      # Component 2: 2 → 3
    3: []
}
# Expected: NO CYCLE

# Test cases
test_cases = [
    (cycle_3_nodes, True, "Simple 3-node cycle"),
    (no_cycle_3_nodes, False, "Linear chain"),
    (self_loop, True, "Self loop"),
    (mixed_components, True, "Mixed components"),
    (tree_structure, False, "Tree structure"),
    (complex_cycle, True, "Complex cycle"),
    (empty_graph, False, "Empty graph"),
    (disconnected_no_cycle, False, "Disconnected no cycle")
]

for adj_list, expected, description in test_cases:
    result = has_cycle(adj_list)
    status = 'RIGHT' if result == expected else 'WRONG'
    print(f"{description}: {status}")