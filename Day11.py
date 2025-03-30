#File Handling

read_file = open("D:/Dev/Python Learning/day11.txt", 'r')
print(read_file.read())


write_file = open("D:/Dev/Python Learning/day11.txt", 'w')
write_file.write("Completely new text")


app_file = open("D:/Dev/Python Learning/day11.txt", 'a')
app_file.write(" Append to this file")
