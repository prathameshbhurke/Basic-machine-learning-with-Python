n1 = int(input())
inp1 =  set(map(int, (input().split())))
n2 = int(input())
inp2 = set(map(int, (input().split())))

res = inp1.union(inp2)

print(len(res))