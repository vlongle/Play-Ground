# Compute fibonnaci in O(N) using memoization MIT 6.006 Fall 2011 lec 19


def fib(n):
    fib_bb =1 # fib(n-2) a.k.a back back
    fib_b = 1 # fib(n-1) a.k.a back
    for i in range(n-2):
        temp = fib_b
        fib_b += fib_bb
        fib_bb = temp
    return fib_b

print(fib(7))