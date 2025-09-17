sentence = input()
decode = ""
i = 0

while i < len(sentence):
    decode = decode + sentence[i]
    if sentence[i] in "aeiou":
        i = i + 3
    else: 
        i = i + 1

print(decode)
