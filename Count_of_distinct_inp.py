"""
Input;:
7
UK
China
USA
France
New Zealand
UK
France

7 is the number of countries as input.

Ans: 5

"""
#Solution 2 is better because it does not check the whole list to find the count.


def count_country1(no,inp):
    s = []
    for x in inp:
        if x not in s:
            s.append(x)

    print(len(s))


def count_country2(no,inp):
    res = []
    res = list(set(inp))
    print(len(res))


if __name__ == '__main__':
    no = input()
    n = int(no)
    inp = []
    for i in range(0, n):
        inp.append(input())
    count_country2(n,inp)