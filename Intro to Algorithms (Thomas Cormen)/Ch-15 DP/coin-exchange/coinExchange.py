

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
    return recurse_coin(target_bill, denomination, optimal, soln)

'''Top-down approach using memoization '''
def recurse_coin(target_bill, denomination, optimal, soln):
    # If it's a subproblem we already solved, simply return the result
    if target_bill in optimal:
        return (optimal[target_bill], [target_bill])
    
    # Otherwise, it's a new subproblem to be solved
    min_coins = 9999999
    min_cash = 0
    for cash in denomination: # loop through all possible choices for the first bill
        if target_bill >= cash: # target have to be larger than cash to obtain a valid soln
            sub = recurse_coin(target_bill - cash, denomination, optimal, soln)[0] + 1
            if min_coins > sub:
                min_coins = sub
                min_cash = cash

    optimal[target_bill] = min_coins
    if min_coins != 9999999: # find a valid soln
        soln[target_bill] = [min_cash] + soln[target_bill-min_cash]
    else: # meaning the above "for-loop cash in denomination" fails to find a valid soln ---> No soln is possible
        soln[target_bill] = [None]
    return (min_coins, soln)


''' This is an example '''
denomination = [3,9,15]
target_bill = 16
print(DPCoin(target_bill, denomination)[1]) # This should return None beacause 16 is not possible to be changed by 3,9 or 15
