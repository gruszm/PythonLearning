class myClass:
    variable = "duh"

    def __init__(self, variable2):
        self.variable2 = variable2

    def func(self):
        print("I say %s and %s" % (self.variable, self.variable2))

class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def introduce(self):
        print("Hello, my name is %s %s" % (self.firstName, self.lastName))

obj = myClass("blah")
obj.func()

p = Person("Mike", "Hawk")
p.introduce()

del obj, p