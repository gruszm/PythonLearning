from statistics import variance
from tkinter import Variable


class myClass:
    variable = "duh"

    def func(self):
        print("I say %s" % self.variable)

obj = myClass()
obj.func()