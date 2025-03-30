# choice - login, register
# if register, get username, strore the username in a file
# if login, get username, check if it exist in the file

choice = input("Would you like to login or register?:\n1.Register\n2.Login\n> ")
if choice == '1': 
    username = input('Enter your username to be stored: ')
    login_file = open('D:/Dev/Python Learning/Activity/db.txt', 'a')
    login_file.write(f',{username}')
    login_file.close()
elif choice == '2':
    username = input('Enter your username: ')
    login_file = open('D:/Dev/Python Learning/Activity/db.txt', 'r')
    read = login_file.read()
    users = read.split(',')
    for user in users:
        if user == username:
            print(f'Welcome {username}!')
            break
        else:
            print('User doesn\'t exist')
            break
    login_file.close()
else:
    print('Invalid input')



