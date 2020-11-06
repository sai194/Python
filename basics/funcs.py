def add(a: int, b: int) -> int: # arg are not type checked like java but there are options to enforce
    return a + b

print(add(1,2))
print(add("Fred", "Jones"))

def show(a, b, *args, **kwargs):
    print(f"a is{a}, b is {b}")
    print(type(args))
    for a in args:
        print(a)
    print(type(kwargs))
    for i in kwargs.items():
        print(i)

show(3,4,5,6,7,8, fred="jones", count=3)
l = [9,8,7]
show(5,4, *l)
