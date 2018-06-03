from itertools import combinations
from itertools import combinations_with_replacement

def comb(n1,inp):
    for i in range(1, n1+1):
        for j in sorted(list(combinations(inp, i))):
            print(''.join(j))

def comb2(n1,inp):
    for j in sorted(list(combinations_with_replacement(inp, n1))):
        print(''.join(j))

if __name__ == '__main__':
    a = input()
    a1 = list(a.split())
    inp = sorted(list(a1[0]))
    n1 = int(a1[1])
    comb(n1,inp)
    print("Now with replacement")
    comb2(n1,inp)
