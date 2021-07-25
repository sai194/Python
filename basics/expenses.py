expenses = [10.50, 8, 5, 25, 30, 5, 3]
total = 0

for x in expenses:
    total = total + x

# default separator is space
print('You spent: $', total, sep='')

total = sum(expenses)
print('You spent: $', total, sep='')