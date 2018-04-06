''' use dynamic programming & binary tree to produce O(n^2)
    for an optimization problem (rod-cutting, Intro to Algorithm by Thomas H. Cormen)
'''

import timeit



def brute_force(h, price):
    print("Brute force yeah!!")

def solve_tree(h, price):
    opti = {}
    opti[1] = price[1]
    for i in range(2,h+1):
        opti[i] = tranverse_tree(i, opti, price)
    return opti




def tranverse_tree(h, opti, price):
    ''' Exploit suboptimal structure to tranverse tree height h'''
    optimal_node = [None]*h
    optimal_node[0] = price[h] # h = n
    for i in range(1,h):
        optimal_node[i] = max(optimal_node[i-1], price[h-i]+opti[i])
    return optimal_node[h-1]


price = {1:1, 2:5, 3:8, 4:9, 5:10, 6:17, 7:17, 8:20, 9:24, 10:30} # price[length] = corresponding price
opti = {1:1, 2:5, 3:8}
print(solve_tree(9, price))


