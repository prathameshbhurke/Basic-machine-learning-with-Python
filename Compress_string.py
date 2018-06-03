"""
Sample Input
1222311
Sample Output
(1, 1) (3, 2) (1, 3) (2, 1)

Explanation
First, the character  occurs only once. It is replaced by . Then the character  occurs three times, and it is replaced by  and so on.
Also, note the single space within each compression and between the compressions.
"""


def compress1(inp):
    i = 0
    j = 0
    c = 0
    tup = []

    while i < len(inp):
        c= 0
        while j < len(inp):
            if inp[i] == inp[j]:
                j = j + 1
                c = c + 1
            else:
                break
        tup.append((c,int( inp[i])))
        i = j

    print(*tup)


if __name__ == '__main__':
    inp = list(input())
    compress1(inp)
