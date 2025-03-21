a = 30
b = 45
c = 35

if a > b:
    print("A is Larger")
    if a > c:
        print("A is the Largest")
    else:
        print("C is the largest")
elif b > a:
    print("B is larger")
    if b > c:
        print("B is largest")
    else:
        print("C is largest")
else:
    print("C is largest")


