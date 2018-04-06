


def decorator(someFun):
    print("decorator called")
    def wrapper(*args, **kwargs):
        print("wrapper called")
        print(args)
        print(kwargs)
        return func(*args, **kwargs)
    return wrapper


@decorator
def func(iq, parent = "Le", child = "Long"):
    print("Func called")
    print(parent)


# print("func(120): " , func(120))

# a = decorator(func)
# print(a)
# a(120)
func()
# a = func
# print(a)
# a(120)
