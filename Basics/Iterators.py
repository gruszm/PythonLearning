tup = (1, 2, 3, 4, 5)

it = iter(tup)

print(next(it))
print(next(it))
print(next(it))

print()

tup2 = (2, 4, 6, 8, 10)

it2 = tup2.__iter__()

print(it2.__next__())
print(it2.__next__())

print()


class EverySecondElementIterable:
    def __init__(self, list):
        self.funcList = []

        i = 0
        while i < len(list):
            if i % 2 == 1:
                i += 1
                continue
            else:
                self.funcList.append(list[i])
                i += 1

    def __iter__(self):
        self.currentIterID = 0
        return self

    def __next__(self):
        if self.currentIterID < len(self.funcList):
            self.currentIterID += 1
            return self.funcList[self.currentIterID - 1]
        else:
            raise StopIteration


everySecond = EverySecondElementIterable([1, 2, 3, 4, 5, 6, 7, 8])

it = iter(everySecond)

for x in everySecond:
    print(x)