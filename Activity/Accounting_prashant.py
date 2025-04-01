# Accounting- use file handling
# choice - login, register
# if register,get username and password, store the username in a file
# if login, get username and password, check if it exist in the file
# if user is valid then show them 2 options, 1,check balance, 2. add balance
# if option is add, ask for the amount to add and add it to the user's balance file {username:balance}
# if option is check, print the amount of the user if balance is present in the file, if not print "no balance"
# if user is not valid, print "invalid user"

def check_balance(username):
    f = open('money.txt', 'r')
    data = f.read()
    # unit = ['ram:123', 'hari:123']
    unit = data.split(',')
    # while we don't find the right match for username, we keep on looping using valid
    valid = False
    for i in unit:
        uname = i.split(":")
        # check if the usernames match
        if uname[0] == username:
            valid = True
            b = uname[1]
    if valid:
        print(f'Your balance is: Rs {b}')
    else:
        print('Not a valid user!')

def add_balance(username):
    add = int(input('How much would you like to add?: Rs.'))
    # first open in read 
    f = open('money.txt', 'r')
    data = f.read()
    unit = data.split(',')
    valid = False
    # updated_data is overwrite the file as a whole so we store one updated amount and others remain unchanged
    updated_data = []
    for i in unit:
        uname = i.split(':')
        if uname[0] == username:
            valid = True
            new = int(uname[1]) + add
            updated_data.append(f'{username}:{new}')
        else:
            updated_data.append(i)
    # when the operation is complete, we overwrite the file with new changed data
    if valid:
        m = open('money.txt', 'w')
        # since updated_data is a list, we need to convert the content into string seperated by ,
        m.write(','.join(updated_data))
        print(f"Rs. {add} added successfully!")
    else:
        print("User not found!")

def register():
    # when registering, we create two files one for username and other for money with the same username
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    f = open('users.txt', 'a')
    f.write(f"{username}:{password},")
    f.close()
    money = input('Enter your initial balance: ')
    m = open('money.txt', 'a')
    m.write(f"{username}:{money},")
    m.close()

def login():
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    f = open('users.txt', 'r')
    data = f.read()
    unit = data.split(',')
    is_logged = False
    for i in unit:
        uname = i.split(':')
        if uname[0] == username and uname[1] == password:
            # if uname and pw is not what we entered, then skip to the next value cause is_logged is False
            is_logged = True

    if is_logged:
        print('Logged in')
        while True:
            c = input('1. Check balance\n2. Add balance\n>')
            if c == '1':
                check_balance(username)
            elif c == '2':
                add_balance(username)
            else:
                print('Invalid input!')
            con = input('Would you like to continue?[y/n]: ').lower()
            if con != 'y':
                break

    else:
        print('Invalid Credentails!')

choice = input('1.Register\n2.Login')
if choice == '1':
    register()
elif choice == '2':
    login()
else:
    print('Not a valid choice!')