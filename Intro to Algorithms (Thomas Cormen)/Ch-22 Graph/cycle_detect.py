
# Python default parameter is only evaluated ONCE!!
def topo_sort(s,graph, visit = [], parent = {}, finished_stack = []):
    print(s, finished_stack)
    if s not in visit:
        visit.append(s)
    for v in graph[s]:
        if v not in visit:
            parent[v]  = s
            topo_sort(v, graph, visit, parent, finished_stack)
    finished_stack.append(s) # appending is key
    return (visit,finished_stack)

def topo_exhaust(graph, visit = [], finished_stack = []):
    for s in graph:
        if s not in visit:
            visit,finished_stack = topo_sort(s, graph) # we set finished_stack again, somehow we pass the finished stack to topo_sort unwillingly !
            # because in topo_sort, append directly change the finished_stack struct
    return (visit, finished_stack)

# graph = {
#     'A':['B'],
#     'B': ['C'],
#     'C': []
# }

graph = {
    'CS61': ['CS62'],
    'CS62': ['Data struct'],
    'Data struct': ['AI'],
    'Stat': ['AI', 'Data struct'],
    'Cal': ['Stat'],
    'AI': []
}

# print(topo_sort('Cal', graph))
print(list(reversed(topo_exhaust(graph)[1])))

# def test1(name = []):
#     print(name)
#     return name
#
# def test2():
#     name = [3,2,3]
#     name = test1()
#     print(name)
#
# test2()