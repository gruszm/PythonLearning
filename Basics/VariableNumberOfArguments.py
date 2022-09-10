def func1(one, two, *rest):
    print("%s %s %s" % (one, two, rest))

def func2(one, two, **rest):
    if rest.get("first") == True:
        print(one)
    if rest.get("second") == True:
        print(two)


func1(1, 2, 3, 4, 5)
func1(2, "two", "a", "b", 4.3)

func2(1, 2, first = True, second = True)