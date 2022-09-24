try:
    print(x)
except:
    print("x not defined")

x = 3

while True:
    print(x)
    x -= 1

    if x < 0:
        raise Exception("x is lower than 0 which is forbidden")