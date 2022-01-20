print('Welcome to State bank of Poland')

pin = int(input('Please write your four digit pin number: '))
money = 25000

if pin == 1234:

    print('1 - Withdraw')
    print('2 - check your balance account')
    print('3- Fast cash')

    choosetransaction = int(input('Please choose transactions: '))

    if choosetransaction == 1:
        withdraw =int(input('Enter withdraw amount: '))

        if withdraw < money and withdraw%100 == 0:
            print('Please take your withdraw amount:',withdraw)
        else:
            print('Invalid cash')

    elif choosetransaction == 2:
        print('Your availabe amount: ',money)

    elif choosetransaction == 3:
        print('1 -> 5000')
        print('2 -> 10000')
        print('3 -> 15000')
        print('4 -> 20000')
        cashoption = int(input('Please enter fast cash option: '))

        if cashoption == 1 and money > 5000:
            print('Please take cash 5000')

        elif cashoption == 2 and money > 10000:
            print('Please take you money 10000')

        elif cashoption == 3 and money > 15000:
            print('Please take your money 15000')

        elif cashoption == 4 and money > 20000:
            print('Please take your money 20000')

        else:
            print('Invalid cash option')
            print('Wrong choice')

    else:
         print('Wrong pin number,please try again')





