from pandas import DataFrame # DataFrame.to_excel lib

def enter_Q(n):
    arr = []
    i = 1
    while len(arr) < n:
        inp = input("Enter for # " + str(i) + " : ")
        i +=1
        if inp != 'p':
            arr.append(inp)
        else:
            arr.pop()
            i -=2
            print("Enter again for # " + str(i)+ " : ")
    print()
    return arr

def compare(l1, l2, name):
    if len(l1) != len(l2):
        raise Exception("Mismatched lenght")
    else:
        list_false = []
        i = 0
        true_answ = 0
        for i in range(len(l1)):
            if l1[i] != l2[i]:
                list_false.append("false")
            else:
                list_false.append("true")
                true_answ +=1
        df = DataFrame({"MyChoice":l1, "Correct": l2, "T/F": list_false})
        df.to_excel(name, sheet_name = 'sheet1', index = True)
        print("True:", str(true_answ), "/", str(len(l1)))
    return list_false



l1 = enter_Q(35)
l2 = enter_Q(35)

print(compare(l1,l2, 'PhysicsCE&M2012.xlsx'))