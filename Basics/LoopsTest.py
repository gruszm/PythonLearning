for x in range(5):
    print(x)

for x in range(5, 11):
    print(x)

counter = 10
while counter > 0:
    print(counter)
    counter -= 1

for x in range(11):
    print(x)
    if x == 5:
        break

for x in range(11):
    if x % 2 == 0:
        continue
    else:
        print(x)