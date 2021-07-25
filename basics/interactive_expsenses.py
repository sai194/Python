total = 0
num_expenses = int(input('# of expenses: '))
expenses = []

for i in range(num_expenses):
    expenses.append(int(input('enter expense: ')))

total = sum(expenses)
print('You spent: $', total, sep='')