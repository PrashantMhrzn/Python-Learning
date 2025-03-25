# Exception Handling
try:
    a = int(input("Enter: "))
    print(a)

except ValueError as err:
    print(err)

# except (ValueError, NameError) as error:
#     print(f"A {type(error).__name__} has occurred.")