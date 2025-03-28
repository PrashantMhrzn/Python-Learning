
# Activity - 
# implement while loop in calculator from day 5
# ask use if they want to continue, if yes continue the calculation, if no end the program
# Make it function based

def add(v1, v2):
    return v1 + v2

def sub(v1, v2):
    return v1 - v2

def mul(v1, v2):
    return v1 * v2

def div(v1, v2):
    return v1 / v2


while True:
    try:
        inp_a = int(input("Enter first number: "))
        inp_b = int(input("Enter second number: "))
        op = input("Enter operator:(+/-/*/ /) ")

        if op == '+':
            sum = add(inp_a, inp_b)
            print(f"Sum : {sum}")
        elif op == '-':
            diff = sub(inp_a, inp_b)
            print(f"Difference : {diff}")
        elif op == '*':
            mul = mul(inp_a, inp_b)
            print(f"Product : {mul}")
        elif op == '/':
            div = div(inp_a, inp_b)
            print(f"Divide : {div}")
        else:
            print("Invalid operator")

    except:
        print("Error occured, Please enter correct values!")

    con = input("Do you want to continue?[y/n]: ").upper()
    if con != 'Y':
        break


