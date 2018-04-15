



# Bugs at visit
# no repetition --> store visit to keep track of nodes
def DPExchange(source, rate, target, curr, visit = [], soln = {}):
    if source == target:
        soln[(source, target)] = 1
        return 1
    if source in visit:
        return soln[(source, target)]

    max_val = -9999
    visit.append(source)
    for currency in curr:
        if currency not in visit:
            max_val = max(max_val, rate[(source, currency)]*DPExchange(currency, rate, target, curr, visit, soln))

    soln[(source, target)] = max_val
    return max_val


curr = ['v', 'r', 'c', 'usa']
rate = {('v', 'v'):1,
        ('v', 'r'):2,
        ('v', 'c'): 1.5,
        ('v', 'usa'): 0.5,
        ('r', 'v'): 1/2,
        ('r', 'r'): 1,
        ('r', 'c'): 2,
        ('r', 'usa'): 0.4,
        ('c', 'viet'): 1/(1.5),
        ('c', 'r'): 1 / 2,
        ('c', 'c'): 1,
        ('c', 'usa'): 1 / (1.7),
        ('usa', 'viet'): 2,
        ('usa', 'r'): 1/(0.4),
        ('usa', 'c'): 1.7,
        ('usa', 'usa'): 1,

        }


# print(rate[('v', 'r')]*rate[('r', 'c')]*rate[('c', 'usa')])

print(DPExchange('v', rate, 'usa', curr))