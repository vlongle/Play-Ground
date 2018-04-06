


# factor in the cost of making one cut
def bottomUp(p, n, cost = 0):
    opti = {}
    opti[0] = 0
    for i in range(1,n+1):
        q = -999
        for j in range(1, i+1):
            if j == i:
                q = max(q, p[j])
            else:
                q = max(q, p[j] + opti[i-j]-cost)
        opti[i] = q
    return opti[n]



def topDown(p, n, cost = 0, opti = {}):
    q = -999
    if n == 0:
        q = 0
    if n in opti:
        q =  opti[n]
    else:
        for i in range(1,n):
            q = max(q, p[i] + topDown(p, n-i, cost, opti)-cost) # take cost into account
        q = max(q, p[n]) # handle the don't cut separately
        opti[n] = q
    return q



p = [0,1,5,8,9,10,17,17,20,24,30]
cost = 1
print(topDown(p, 4, cost = 4))

print(bottomUp(p, 4, cost = 4))