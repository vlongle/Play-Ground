

'''Solve the problem of coin-exchange by Dynamic Programming
`denomination` is a list that stores all denomination available to us.
`optimal` is a dict that stores the minimum target_bills necessary for the target target_bill.
`soln` is a dict that stores the specific solutions to achieve the optimal soln in dict  ` optimal`
'''
def DPCoin(target_bill, denomination, optimal = {}, soln = {}):
    # basic initialization of optimal & soln dictionary
    optimal[0] = 0
    for cash in denomination:
        optimal[cash] = 1
        soln[cash] = [cash]
    return DPCoin(target_bill, denomination, optimal, soln)

'''Top-down approach using memoization '''
def recurse_coin(target_bill, denomination, optimal, soln):
    if target_bill in optimal:
        return (optimal[target_bill], [target_bill])

    min_coins = 9999999
    min_cash = 0
    for cash in denomination: # loop through all possible choices for the first bill
        if target_bill >= cash:
            sub = recurse_coin(target_bill - cash, denomination, optimal, soln)[0] + 1
            if min_coins > sub:
                min_coins = sub
                min_cash = cash
    optimal[target_bill] = min_coins
    soln[target_bill] = [min_cash] + soln[target_bill-min_cash]
    return (min_coins, soln)


denomination = [1,9,15]
target_bill = 16

a = [12,34]
b = [69]


print(DPCoin(target_bill, denomination)[1][target_bill])