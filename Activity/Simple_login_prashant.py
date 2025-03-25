# create a dictionary containing username and password, username as key and password as value
# ask user for username and password
# check if the username and password are in dictionary
# if yes the print login success, else invalid credentials

db = {'user1': 'potato123','user2': 'tomato123','user3': 'flower123','user4': 'fish123',}

uname = input("Enter your username: ")

if uname in db.keys():
    pw = input("Enter your password: ")
    if db.get(uname) == pw:
        print('Login Success')
    else:
        print('Invalid Password')
else:
    print("Username Doesn't exist!")

