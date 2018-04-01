


# This algorithm doesn't guarantee shortest path !!
# Use stack structure 
def BFS(s, graph):
    levels = {s:0}
    stack = [s]
    while len(stack ) > 0:
        parent = stack.pop()
        for v in graph[parent]:
            if v not in levels:
                levels[v] = levels[parent] + 1
                stack.append(v)
    return levels

# Depth-first search
def DFS(s, graph, visit = []):
    if s not in visit:
        visit.append(s)
    for v in graph[s]:
        if v not in visit:
            visit.append(v)
            DFS(v, graph, visit)
    return visit

def visit_all(graph):
    visit = []
    for v in graph:
        visit += DFS(v, graph)
    return set(visit)






graph = {'A':[ 'B'],
         'B': ['A', 'C', 'D'],
         'C': ['B', 'D'],
         'D': ['C', 'B'],
         'E': ['F'],
         'F': ['E']
}
visit = ['A']
print(BFS('A', graph))
print(DFS('A', graph))
print(visit_all(graph))