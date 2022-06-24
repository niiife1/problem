size = int(input())

matrex = []

for _ in range(size):
     row = [int(x) for x in input().split(', ')]
     matrex.append([x for x in row if x % 2 == 0])
print(matrex)
