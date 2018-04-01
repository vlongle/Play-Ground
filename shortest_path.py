


# This algorithm doesn't guarantee shortest path !!
# Use stack structure 
def BFS(s, graph):
    parent = 'NIL'
    levels = {'NIL':-1}
    stack = [s]
    while len(stack ) > 0:
        current = stack.pop()
        levels[current] = levels[parent]+1
        parent = current
        for v in graph[current]:
            if v not in levels:
                stack.append(v)
    return levels








graph = {'A':['B'],
         'B': ['A', 'C', 'D'],
         'C': ['B', 'D'],
         'D': ['C', 'B'],
}

print(BFS('A', graph))
