




def shortest_path(s, graph, w, visit = {}, parent = {}):
    if s not in visit:
        visit[s] = 0

    min_weight = 9999999
    min_node = None

    if s in graph:
        for v in graph[s]:
            if min_weight > w[(s,v)]:
                min_weight = w[(s,v)]
                min_node = v


    if min_node != None:
        last_min = min_weight
        parent[min_node] = s
        visit[min_node] = min_weight + visit[s]
        return shortest_path(min_node, graph, w, visit, parent)


    return (visit, parent)

visit = []
graph = {
'A': ['B', 'D', 'E'],\
'B': ['C'],\
'C': ['D', 'F'],\
'E':{'F'}\
}

w = {('A', 'B'):4, ('A', 'D'):10, ('A', 'E'): 9,\
('B','C'):4, ('C', 'D'):1, ('C', 'F'):10, \
('E', 'F'):2
}

s = 'A'
while s not in visit:
    visit, parent = shortest_path(s, graph, w)
print(visit, parent)