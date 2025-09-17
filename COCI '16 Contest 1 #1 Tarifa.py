x = int (input())
n = int (input())

remaining = 0

for i in range (n):
    used = int (input())
    remaining = x + remaining - used

print(x + remaining)
