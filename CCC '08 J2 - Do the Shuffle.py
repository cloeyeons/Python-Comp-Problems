original = "ABCDE"
button = 0

while button!= 4: 
    button = int(input())
    number = int(input())
    for i in range(number):
        if button == 1:
            original = original[1:] + original[0]
        elif button == 2:
            original = original[-1:] + original[:-1]
        elif button == 3:
            original = original[1] + original[0] + original[2:]

output = ""
for i in original:
    output = output + i + " "

print(output[:-1])

