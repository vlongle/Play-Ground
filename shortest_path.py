import queue


# This algorithm doesn't guarantee shortest path !!
# Use stack structure 
def BFS(s, graph):
    levels = {s:0}
    backtrack = {s: None}
    q = queue.Queue()
    q.put(s)
    while not q.empty():
        parent = q.get()
        for v in graph[parent]:
            if v not in levels:
                levels[v] = levels[parent] + 1
                backtrack[v] = parent
                q.put(v)
    return (levels, backtrack)

# Depth-first search
def DFS(s, graph, visit = []):
    if s not in visit:
        visit.append(s)
    for v in graph[s]:
        if v not in visit:
            visit.append(v)
            DFS(v, graph, visit)
    return visit

# visit all nodes in the graph
def visit_all(graph):
    visit = []
    for v in graph:
        visit += DFS(v, graph)
    return set(visit)

# s->v
def shortest_BFS_path(s,v, graph):
    levels, backtracks = BFS(s, graph)
    path = [v]
    current = v
    while current !=s:
        back = backtracks[current]
        path.append(back)
        current = back
    return path





graph = {'A':[ 'B'],
         'B': ['A', 'C', 'D'],
         'C': ['B', 'D'],
         'D': ['C', 'B'],
         'E': ['F'],
         'F': ['E']
}
visit = ['A']
levels, backtracks = BFS('A', graph)
print(levels, backtracks)
print("shortest",shortest_BFS_path('A', 'A', graph))
print(DFS('A', graph))
print(visit_all(graph))