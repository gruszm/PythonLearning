class myClass:
    variable = "duh"

    def func(self):
        print("I say %s" % self.variable)

obj = myClass()
obj.func()