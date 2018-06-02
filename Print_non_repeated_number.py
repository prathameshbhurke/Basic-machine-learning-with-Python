
def match(n1,inp1):
    d  = {i: inp1.count(i) for i in inp1}

    for k,v in d.items():
        if v == 1:
            print(k)

if __name__ ==  '__main__':
    n1 = map(int, input())
    inp1 = input().split()
    match(n1,inp1)