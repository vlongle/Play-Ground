

# Return the cost of computing Matrix 1 x Matrix 2 & the dimension of the result
def cost(row1, col1, row2, col2):
    if col1 != row2:
        print("Error. Column-row mismatched")
        return -1
    else:
        return row1*col1*col2


# remember to pass begin = 0 and end = len(Arr)-1
def topDown(Arr, begin, end, MIN_VAL = {}, MIN_DIM = {}):
    # initialization & checking
    if begin == end:
        return (0, Arr[begin])
    elif (begin, end) not in MIN_VAL:
        min_val = 999999999999999999 # meant to be infinity
        min_dim = (0,0)
        for cross in range(begin+1, end+1):  # where to place the cross sign of multiply
            left_val, left_dim = topDown(Arr, begin,cross -1)
            right_val, right_dim = topDown(Arr, cross, end)
            cost_combine = cost(left_dim[0], left_dim[1], right_dim[0], right_dim[1])
            total_cost = left_val + right_val + cost_combine
            if total_cost < min_val:
                min_val = total_cost
                min_dim = (left_dim[0], right_dim[1])
        MIN_VAL[(begin, end)] = min_val
        MIN_DIM[(begin, end)] = min_dim
    return (MIN_VAL[(begin, end)], MIN_DIM[(begin, end)])




# def chain(Arr, begin, end, opti = {}):
#     if (begin, end) in opti:
#         return opti[(begin, end)]
#     else:
#         for i in range(begin, end):
#             sub_min = 9999999
#             for j in range():



A = (10,100)
B = (100,5 )
C = (5, 50)
Arr = [(10,100),(100,5 ), (5, 50), (50, 4), (4, 69) ]
di = {(1,2):5}
# print(cost(B[0], B[1], C[0], C[1]))
# print(cost(A[0], A[1], 100, 50))
# print(Arr[0][1])
# # if (1,2) in di:
# #     print(di[(1,2)])

print(topDown(Arr, 0, len(Arr)-1))