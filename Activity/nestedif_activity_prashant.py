# Activity - 
# ask user for their age
# if age is less than 18 print they are not eligible for licenses 
# and ask if they any vehicle they want to get/buy then print some statement
# if age is greater or equal to 18 print they are eligible for licenses 
# and ask if they have any vehicle , if yes print a statement else print a statement

age = int(input("Enter your age: "))

if age < 18:
    print("You are NOT eligible for a liscence yet!")

    vehicle = input("Do you have any vehicles you wish to buy?(y/n): ")
    if vehicle == 'y':
        choice = input("What vehicle would you like to buy? ")
        print(f"{choice} is a great choice! Not long now.")
    elif vehicle == 'n':
        print("Goodluck!")
    else:
        print("Enter either 'y' or 'n' !!!")

elif age >= 18 and age <= 100:
    print("You are eligible for a liscence! yayy")

    vehicle = input("Do you own any vehicle?(y/n): ")
    if vehicle == 'y':
        print("Becareful on the road")
    elif vehicle == 'n':
        print("Lets get you a good car!")
    else:
        print("Enter either 'y' or 'n' !!!")

else:
    print("Please enter correct values.")