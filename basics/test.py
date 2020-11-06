x = 0b0101010
print(x)
print(type(x))
print(None)
print(type(None))

x = "hello"
print(x)
x = 'hello'
print(x)
x = x + " test " \
        " \n peek"
print(x)

y = 99
out = "the value of {0}".format(y)
print(out)


print(10/3)
print(10//3)
print(10.5//3)

x = 5
x += 3
print(x)
x += 3.0
print(x)

x = "hello"
y = "hello"
print(x==y)
print(x is y)
y = "he"
y = y + "llo"
print(x==y)
print(x is y)

x = 0b00001111
y = 0b01010101
print(x, y)
print(x & y)
print(x | y)
print(x ^ y)
print(True & x)
print(True and True)
print(True or False)
print(3 or 5)
