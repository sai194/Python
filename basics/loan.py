money_owed = float(input('How much do you owe: $'))
apr = float(input('Your apr%: '))
payment = float(input('Your monthly payment: $'))
months = int(input('How many months do you want result to see for? '))

monthly_rate = apr/100/12

for i in range(months):
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid

    if money_owed - payment < 0:
        print('The last payment is: $', money_owed, sep='')
        print('You paid off the amount in moths:', i-1)
        break

    money_owed = money_owed - payment

    print('Paid', payment, 'of which', interest_paid, 'interest paid', end=' ')
    print("Now I owe", money_owed)
