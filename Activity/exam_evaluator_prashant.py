# Activity - Exam evaluator: Ask user to enter a mark, if mark is greater than 90 and less than 100 print smth
# If mark is greater than 80 and less than 90 print smth
# If mark is greater than 70 and less than 80 print smth
# If mark is greater than 60 and less than 70 print smth
# If mark is greater than 50 and less than 60 print smth
# If mark is greater than 40 and less than 50 print smth
# If marks is less than 40 print smth

marks = int(input("Enter your marks: "))

if marks >= 90 and marks <= 100:
    print("A+")
elif marks >= 80 and marks <= 89:
    print("A")
elif marks >= 70 and marks <= 79:
    print("B+")
elif marks >= 60 and marks <= 69:
    print("B")
elif marks >= 50 and marks <= 59:
    print("C+")
elif marks >= 40 and marks <= 49:
    print("C")
elif marks <= 39:
    print("D")
else:
    print("Out of range!")