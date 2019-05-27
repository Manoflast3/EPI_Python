# using graph from dfs.py
# adjacency list
def bfs(graph, start, dest):
    queue, visited = [start], set()
    while (queue):
        v = queue.pop(0)
        if (v not in visited):
            visited.append(v)
            # add all the adjacent nodes to v
            queue.extend(graph[v] - v)
    return visited