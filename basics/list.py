x = True
print(x)

print(str(True))
print(int(True))

if (1):
    print("true")
else:
    print("false")

if ([]):
    print("true")
else:
    print("false")

if ([1, 2]):
    print("true")
else:
    print("false")

l = [0, 1, 2, 3, 4, 5, 6, 7]
print(l)
print(type(l))
print(l[0])
print(l[-1])
print(l[-2])
print(l[3:6])
print(l[2:8:2])
print(l[::2])
l.sort()
print(l)
l.sort(reverse=True)
print(l)
a, b, c = [1, 2, 3]
print(a, b, c)

# basics again

acronyms = ['LOL', 'IMO', 'IMHO', 'LMAO']
for acronym in acronyms:
    print(acronym)
