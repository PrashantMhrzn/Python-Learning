
# Activity - 
# implement while loop in calculator from day 5
# ask use if they want to continue, if yes continue the calculation, if no end the program

try: 
    while True:
        inp_a = int(input("Enter first number: "))
        inp_b = int(input("Enter second number: "))

        op = input("Enter operator:(+/-/*/ /) ")

        if op == '+':
            res = inp_a + inp_b
            print(f"Sum : {res}")
        elif op == '-':
            res = inp_a - inp_b
            print(f"Difference : {res}")
        elif op == '*':
            res = inp_a * inp_b
            print(f"Product : {res}")
        elif op == '/':
            res = inp_a / inp_b
            print(f"Divide : {res}")
        else:
            print("Invalid operator")

        con = input("Do you want to continue?[y/n]: ").upper()
        if con != 'Y':
            break

except:
    print('Error occured')

