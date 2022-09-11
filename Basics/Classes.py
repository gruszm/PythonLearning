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

class Employee(Person):
    def __init__(self, firstName, lastName, salary):
        super().__init__(firstName, lastName)
        self.salary = salary

    def introduce(self):
        super().introduce()
        print("My salary is %s" % self.salary)

obj = myClass("blah")
obj.func()

print()

p = Person("Mike", "Hawk")
p.introduce()

print()

em = Employee("Jake", "Smith", "10000")
em.introduce()

print()

del obj, p, em