from itertools import combinations

def comb(n1,inp):
    for i in range(1, n1+1):
        for j in sorted(list(combinations(inp, i))):
            print(''.join(j))


if __name__ == '__main__':
    a = input()
    a1 = list(a.split())
    inp = sorted(list(a1[0]))
    n1 = int(a1[1])
    comb(n1,inp)