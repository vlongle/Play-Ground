




def DPRecurse(n, price):
    opti = {}
    opti[0] = 0
    path_dict = {0:[None]}
    for i in range(1,n+1):
        max, path = choice(i, opti, price)
        opti[i] = max
        path_dict[i] = [path] + path_dict[i-path]
        # print('i, max, path, path_dict', (i, max, path, path_dict))
    return (opti, path_dict)


''' The rational is as follows:
For a given stick length n, we have only 2 disjoint choices:
- To keep the stick as a whole ---> sell with price[n]
- Make AT LEAST 1 cut (2)

For the (2) scenario, we can consider multiple disjoint events:
- First cut at 1 OR
- First cut at 2 OR
...
- First cut at n-1

Let say, we have the first cut at i, then the optimal price is the price of the stick length i added 
to the OPTIMAL price of how to sell the stick length n-i ---> We have a recursion

With P for optimal price, price for tabular whole stick price, we have the formula
P[n] = max( price[n], price[i] + P[n-i]) for 1 <= i <= n-1


'''
def choice(n, opti, price):
    max = 0
    for i in range(1,n+1): # cut at 1 or 2 or 3 ... or n (basically not cutting)
        new_sum = price[i] + opti[n-i]
        if new_sum > max:
            max = new_sum
            path = i
    return (max, path)

price = {1:1, 2:5, 3:8, 4:9, 5:10, 6:17, 7:17, 8:20, 9:24, 10:30} # price[length] = corresponding price
opti = {0:0, 1:1, 2:5, 3:8}

# print(choice(4,opti, price))

DPRecurse(10, price)
