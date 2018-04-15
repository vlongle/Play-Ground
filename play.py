

f = open('test.txt', 'w')
for i in range(1,35):
    ans = input("answ")
    print(i, "--", ans)
    f.write(str(i) +" -- "+ans)
print("Hi")