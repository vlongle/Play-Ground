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
def DFS(s, graph, visit = [], active = {}, parent = {}):
    if s not in parent:
        parent[s] = None
    if s not in visit:
        visit.append(s)
        active[s] = True # The active dictionary to record back edge
    for v in graph[s]:
        if v in visit and parent[s] != v:
            try: # may encounter Key error v is not in active[]
                if active[v] == True:
                    print("There's a cycle at ", parent)
            except Exception:
                pass
        elif v not in visit:
            parent[v] = s
            DFS(v, graph, visit, active, parent)
    active[s] = False
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




graph = { 'A': ['B'],
          'B': ['C'],
        'C': []
}

print(DFS('A',graph))
# graph = {'A':[ 'B'],
#          'B': ['A', 'C', 'D'],
#          'C': ['B', 'D'],
#          'D': ['C', 'B'],
#          'E': ['F'],
#          'F': ['E']
# }
# visit = ['A']
# levels, backtracks = BFS('A', graph)
# print(levels, backtracks)
# print("shortest",shortest_BFS_path('A', 'D', graph))
# print('DFS', DFS('A', graph))
# print(visit_all(graph))