
from collections import defaultdict, namedtuple
vertex = namedtuple(('v'), ('value1', 'value2'))

# graph representation 
# 

def build_graph(l):
    graph = defaultdict()
    for item in l:
        graph[item.value1] = 
    return graph

def dfs(graph, curr, dest, visited=set()):
    if (curr == dest):
        return True
    else if (curr in visited or curr is not in graph.keys()):
        return False
    visited.add(curr)
    return any(dfs(graph, next, dest) for next in graph[curr])