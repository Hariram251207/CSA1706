def dfs(graph, start):
    visited = set()
    result = []

    def explore(node):
        visited.add(node)
        result.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                explore(neighbor)

    explore(start)
    return result


# First input: Choose graph type
graph_type = input(
    "Enter graph type (directed/undirected): "
).strip().lower()

if graph_type not in ("directed", "undirected"):
    print("Invalid graph type!")
else:
    # Second input: Graph details
    n = int(input("Enter number of vertices: "))
    e = int(input("Enter number of edges: "))

    graph = {i: [] for i in range(1, n + 1)}

    print("Enter edges (u v):")

    for _ in range(e):
        u, v = map(int, input().split())

        graph[u].append(v)

        if graph_type == "undirected":
            graph[v].append(u)

    start = int(input("Enter starting vertex: "))

    if start not in graph:
        print("Invalid starting vertex!")
    else:
        traversal = dfs(graph, start)
        print("DFS Traversal:", " -> ".join(map(str, traversal)))