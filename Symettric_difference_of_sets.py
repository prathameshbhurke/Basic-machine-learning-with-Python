
#Output the symmetric difference integers in ascending order, one per line.

def sym_diff1(no_inp1,a,no_inp2,b):
    str1 = set(a.split())
    str2 = set(b.split())
    a1 = str1.difference(str2)
    a2 = str2.difference(str1)
    re = map(int, list(a1.union(a2)))
    res = sorted(re)
    #print(res)
    for i in range(0,len(res)):
        print(res[i])


def sym_diff2(no_inp1,a,no_inp2,b):
    str1 = set(a.split())
    str2 = set(b.split())
    str_union = sorted(str1.union(str2))
    str_inter = str1.intersection(str2)
    for i in str_union:
        if i not in str_inter:
            print(i)

def sym_diff3(no_inp1, a, no_inp2, b):
    str1 = set(a.split())
    str2 = set(b.split())
    print(sorted(str1.symmetric_difference(str2))

if __name__ == '__main__':
    no_inp1 = input()
    a = input()
    no_inp2 = input()
    b = input()
    #sym_diff1(no_inp1,a,no_inp2,b)
    #print("next function output:")
    #sym_diff2(no_inp1, a, no_inp2, b)
    #print("Last function:")
    sym_diff3(no_inp1, a, no_inp2, b)
