# a = "The light blinded him. but the light shining in his eyes proved him wrong. It came from about 100 feet away and was shining so directly into his eyes he couldn't make out anything about the person holding the light."

# everytime "o" is found in the data, print a "O found"

find_o = "The light blinded him. but the light shining in his eyes proved him wrong. It came from about 100 feet away and was shining so directly into his eyes he couldn't make out anything about the person holding the light."

count = 0
for o in find_o:
    if o == 'o':
        print("O Found!")
        count += 1
print(f'Total Os: {count}')

