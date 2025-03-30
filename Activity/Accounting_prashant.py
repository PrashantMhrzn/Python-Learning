# Accounting
# create a dictionary that stores user data
# create another dictionary that stores user name and balance, username as key 
# and balance as value
# ask user for their credientials
# if user is valid then show them 3 options, 1,check balance, 2. add balance, 3. withdraw balance
# if option is check, print the amount of the user
# if option is add, ask for the amount to add and add it to the user's balance
# if option is withdraw, ask for the amount to withdraw, check if the withdraw amount 
# is less than the balance, if the withdraw amount is less than the balance, subtract 
# the withdraw amount from the balance, else print "insufficient balance"
# if user is not valid, print "invalid user"
choice = input("Would you like to login or register?:\n1.Register\n2.Login\n> ")
if choice == '1': 
    username = input('Enter your username to be stored: ')
    password = input('Enter your password to be stored: ')
    bank_acc = open('D:/Dev/Python Learning/Activity/bank_acc.txt', 'a')
    bank_acc.write(f'{username},{password},')
    bank_acc.close()
    initial_money = int(input('Enter money to be deposited: '))
    money = open('D:/Dev/Python Learning/Activity/money.txt', 'a')
    money.write(f'{initial_money},')
    money.close()
elif choice == '2':
    inp_username = input('Enter your username: ')
    inp_password = input('Enter your password: ')
    bank_acc = open('D:/Dev/Python Learning/Activity/bank_acc.txt', 'r')
    read = bank_acc.read()
    users = read.split(',')
    username = users[::2]
    password = users[1::2]
    credentials = dict(zip(username, password))
    money = open('D:/Dev/Python Learning/Activity/money.txt', 'r')
    read_money = money.read()
    individual_money = read_money.split(',')
    balance = dict(zip(username, individual_money))
    print(balance)
    print(balance.get(inp_username))
    print(credentials)
    if inp_username in credentials.keys():
        if inp_password == credentials.get(inp_username):
            print('LOGGED IN')
            while True:
                choice = input('''
                ****Welcome to your account!***
                1. Check balance
                2. Add balance
                3. Withdraw balance
                >
                ''')        
                # Catch error for wrong input to int values 
                # try:
                if choice == '1':
                    # Calling relevant functions
                    print(f'Your balance is: {balance.get(inp_username)}')
                elif choice == '2':
                    add_amt = int(input('Enter your amount to add to your account: '))
                    new_amt = int(balance.get(inp_username)) + add_amt
                    print(f'Your added new balance is: {new_amt}')
                elif choice == '3':
                    wit_amt = int(input('Enter your amount to withdraw from your account: '))
                    # Checking if the amount entered can be withdrawn
                    if int(balance.get(inp_username)) >= wit_amt:
                        deducted_amt = int(balance.get(inp_username)) - wit_amt
                        print(f'Your new balance is: {deducted_amt}')
                    else:
                        print('Insufficient Balance!')
                else:
                    print('Invalid input!')
                # except:
                #     print('Enter number value to be added!')

                choice = input('Do you want to keep using the app?[y/n]: ').upper()
                if choice != 'Y':
                    break
        else:
            print('Password for the given username doesn\'t match! Enter a valid password!')
    else:
        print('Username not found in database! Please enter a valid username!')
    bank_acc.close()
else:
    print('Invalid input')

# account = {'ram': 10000, 'hari': 900000, 'u':890000}


# def show_balance(username):
#     return account.get(username)

# def add_balance(username, amt):
#     add_amt = account.get(username)
#     new_balance = add_amt + amt
#     return new_balance

# def wit_balance(username, amt):
#     initial_balance = account.get(username)
#     new_balance = initial_balance - amt
#     return new_balance


       