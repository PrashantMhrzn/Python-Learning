#File Handling

# read_file = open("D:/Dev/Python Learning/day11.txt", 'r')
# print(read_file.read())


# write_file = open("D:/Dev/Python Learning/day11.txt", 'w')
# write_file.write("Completely new text")


# app_file = open("D:/Dev/Python Learning/day11.txt", 'a')
# app_file.write(" Append to this file")

choice = input("Would you like to login or register?:\n1.Register\n2.Login\n> ")
if choice == '1': 
    username = input('Enter your username to be stored: ')
    password = input('Enter your password to be stored: ')
    login_file = open('D:/Dev/Python Learning/Activity/bank_acc.txt', 'a')
    login_file.write(f'{username},{password},')
    login_file.close()
elif choice == '2':
    inp_username = input('Enter your username: ')
    inp_password = input('Enter your password: ')
    login_file = open('D:/Dev/Python Learning/Activity/bank_acc.txt', 'r')
    read = login_file.read()
    users = read.split(',')
    username = users[::2]
    password = users[1::2]
    credentials = dict(zip(username, password))
    print(users)
    print(username)
    print(password)
    print(credentials)
    if inp_username in credentials.keys():
        if inp_password == credentials.get(inp_username):
            print("Logged in")
        else:
            print('Password for the given username doesn\t match! Enter a valid password!')
    else:
        print('Username not found in database! Please enter a valid username!')
    login_file.close()
else:
    print('Invalid input')