

def foo(pos):
    if pos < 0:
        raise ValueError("Must be a pos")
    else:
        return pos


print(foo(-1))