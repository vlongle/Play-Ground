

# Return the cost of computing Matrix 1 x Matrix 2 & the dimension of the result
def cost(row1, col1, row2, col2):
    if col1 != row2:
        print("Error. Column-row mismatched")
        return -1
    else:
        return row1*col1*col2


# remember to pass begin = 0 and end = len(Arr)-1
def topDown(Arr, begin, end, MIN_VAL = {}, MIN_DIM = {}, soln = {}):
    # initialization & checking
    if begin == end:
        return (0, Arr[begin], soln)
    elif (begin, end) not in MIN_VAL:
        min_val = 999999999999999999 # meant to be infinity
        min_dim = (0,0)
        for cross in range(begin+1, end+1):  # where to place the cross sign of multiply
            left_val, left_dim, soln = topDown(Arr, begin,cross -1)
            right_val, right_dim, soln = topDown(Arr, cross, end)
            cost_combine = cost(left_dim[0], left_dim[1], right_dim[0], right_dim[1])
            total_cost = left_val + right_val + cost_combine
            if total_cost < min_val:
                min_val = total_cost
                min_dim = (left_dim[0], right_dim[1])
                soln[(begin, end)] = cross
        MIN_VAL[(begin, end)] = min_val
        MIN_DIM[(begin, end)] = min_dim
    return (MIN_VAL[(begin, end)], MIN_DIM[(begin, end)], soln)




# def chain(Arr, begin, end, opti = {}):
#     if (begin, end) in opti:
#         return opti[(begin, end)]
#     else:
#         for i in range(begin, end):
#             sub_min = 9999999
#             for j in range():

'''Goal, to split into a sequence of i,j that is doable '''

# A = (10,100)
# B = (100,5 )
# C = (5, 50)
# Arr = [(30,35), (35,15), (15,5), (5,10), (10,20), (20,25)]
# di = {(1,2):5}





# print(cost(B[0], B[1], C[0], C[1]))
# print(cost(A[0], A[1], 100, 50))
# print(Arr[0][1])
# # if (1,2) in di:
# #     print(di[(1,2)])







# MIN_VAL, MIN_DIM, soln = topDown(Arr, 0, len(Arr)-1)
# print(soln)
# print('MIN_VAL',MIN_VAL)
# print(soln[(0,len(Arr)-1)])
# print(soln[(0,2)])
# print(soln[(3,5)])

# print(soln[1,2)])