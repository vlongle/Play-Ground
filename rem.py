
m = 5
n = 3
# k = 0




def EuclidTime(m,n):
    while True:
        r = m%n
        if r == 0:
            break
        else:
            m = n
            n = r

    return n


def extendedEuclid(m,n):
    (a,b) = (1,0)
    (c,d) = (0,1)
    T = 0
    while True:
        T +=1  # count the remainder as 1 time step
        print(m,n, T)
        r = m % n
        q = m // n
        T += 1 # count the checking r = 0 ? as 1 time step
        if r == 0:
            break
        else:

            T +=1 # count the reducing as 1 time step
            m = n
            n = r

            (h,k) = (a,b)
            (a,b) = (c,d)
            c = h - q*c
            d = k - q*d

    return (n, a,b, T)


# print(m,n)
result = extendedEuclid(m,n)

print(result)