# loop
# while loop
a = 0
b = 5
c = 8

while a < b:
    print("while loop")
    a+= 1
    while c > b:
        print("Inside while")
        c -= 1
        while c == 7:
            print("Double nested while")
            c -= 1