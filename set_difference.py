
def diff1(n1,inp1,n2,inp2):
    all = inp1.union(inp2)
    s= []
    for x in all:
        if x not in inp2:
            s.append(x)
    print(len(s))

def diff2(n1,inp1,n2,inp2):
    res = inp1.difference(inp2)
    print(len(res))


if __name__ ==  '__main__':
    n1 = input()
    n1 = map(int, n1)
    inp1 = set(map(int, (input().split())))
    n2 = input()
    n2 = map(int, n2)
    inp2 = set(map(int, (input().split())))
    diff2(n1,inp1,n2,inp2)