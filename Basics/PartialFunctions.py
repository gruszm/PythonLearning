from functools import partial

def multiply(x, y):
    return x * y

doubleIt = partial(multiply, 2)

print(doubleIt(3))


def add(x, y, z):
    return x + y + z


addSomething = partial(add, 3, 4)

print(addSomething(5))