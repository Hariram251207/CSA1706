from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


# Get graph input
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of directed edges: "))

graph = {i: [] for i in range(1, n + 1)}

print("Enter directed edges (from_vertex to_vertex):")

for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)  # One-way edge: u -> v

start = int(input("Enter starting vertex: "))

print("BFS Traversal:", " -> ".join(map(str, bfs(graph, start))))