from itertools import product
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))


print(*product(a1,a2))