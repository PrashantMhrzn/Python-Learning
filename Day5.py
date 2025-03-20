# Conditional Statement
# Activity - ask user for their age
# If age is less than 18 print smth
# If age is greater than 18 print another statement
# else, print a statement

age = int(input("Enter your age: "))

if age < 18:
    print("Under the drinking limit!")
elif age > 18:
    print("Good to drink!")
else:
    print("Some more time...")