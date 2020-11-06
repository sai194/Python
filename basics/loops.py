count = 3

if count >2: print("big"); print("I mean it")

while count < 99:
    count += 1
    print("count",count)
    if count == 2:
        break
    print(count, "didn't cause break")
else:
    print("did break")
