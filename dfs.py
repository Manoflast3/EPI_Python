
from collections import defaultdict, namedtuple
vertex = namedtuple(('v'), ('value1', 'value2'))


def build_graph(l):
    graph = defaultdict()
    for item in l:
        graph[item.value1] = 
    return graph