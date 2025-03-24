# Activity - create a list containing usernames, ask user to enter a username
# if the username is in the list, print login else print invalid

usernames = ["first123", "second123","thrid123"]

usr_inp = input("Enter you username: ")

if usr_inp in usernames:
    print("Login Successful!")
else:
    print("Invalid Username!")