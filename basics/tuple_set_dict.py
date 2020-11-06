x = (1,2,3)
print(type(x))
print(x)
print(x[0])
print(x[0:2])

x = 9, 8, 7
print(type(x))
print(x)

def get_tuple():
    return 1, 2, 3

print(get_tuple())
a, b, c = get_tuple()
print(a, b, c)

tup = (1, "two", 3)
print(tup)

a_set = {1,2,3,6,0,1,2,3}
print(a_set)

dict = {"Fred": 1, "Jim": "sss", "Sai": "Yeluri"}
print(type(dict))
print(dict["Sai"])
#print("missing", dict["missing"])#KeyError: 'missing'
print(dict)
