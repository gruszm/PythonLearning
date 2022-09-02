dic = {}
dic["One"] = 1
dic["Two"] = 2
dic["Three"] = 3

dic_simple = {
    "One" : 1,
    "Two" : 2,
    "Three" : 3
}

print(dic)
print()
print(dic_simple)
print()

for name, value in dic.items():
    print("%d is %s" % (value, name))

print()
print(dic_simple["Two"])

dic_simple.pop("Two")
print()
print(dic_simple)