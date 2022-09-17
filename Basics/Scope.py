x = 0

def changeX():
    global x
    x = 1

changeX()
print("%d\n" % x)

def createGlobalVariableY():
    global y
    y = 2

createGlobalVariableY()
print("%d\n" % y)