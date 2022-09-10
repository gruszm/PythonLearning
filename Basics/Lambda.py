lambdaFunc1 = lambda a, b, c : (a + b + c)

print(lambdaFunc1(2, 4, 6))

lambdaFunc2 = lambda name : "Hello %s" % name
print(lambdaFunc2("Mike"))

def lambdaAuxFunc(coeff):
    return lambda a : a * coeff

timesTwoAndAHalf = lambdaAuxFunc(2.5)

print(timesTwoAndAHalf(3))

timesThree = lambdaAuxFunc(3)

print(timesThree(4))