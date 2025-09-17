n = int(input())
village = []
sizes = []

for i in range(n):
    village.append(int(input()))

village.sort()

for i in range(1, n-1):
    left = (village[i] - village[i-1]) / 2
    right = (village[i+1] - village[i]) /2
    size = left + right
    sizes.append(size)

min_size = min(sizes)
print(min_size)
   
