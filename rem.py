
m = 6099
n = 2166
# k = 0

def extendedEuclid(m,n):
    (a,b) = 1,0
    (c,d) = 0,1
    k = 0
    while True:
        if (m>n):
            m -= n
            k +=1
        elif m == n:
            break
        else:
            print("k:", k)
            (temp1, temp2) = (c,d)
            # (c,d) = (a,b) - k*(c,d)
            c = a-k*c
            d = b-k*d
            (a,b) = (temp1, temp2)
            m, n = n, m
            k = 0

    # n is the greatest common divisor, (c,d) s.t. c*m + d*n = gcd(m,n)
    return (n, (c,d))




d = extendedEuclid(m,n)

print(d)
