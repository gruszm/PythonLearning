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