
#This is a word and word is good word

def count_word(inp):
    s = []
    for x in inp:
        s.append((x, inp.count(x)))
    print(s)

def count_word_hash(inp):
    s = {}
    for x in inp:
        if x not in s:
            s[x] = 0
        s[x] +=1
    print(s)

if __name__ == '__main__':
    inp_strg = input()
    inp = inp_strg.split()
    #count_word(inp)
    count_word_hash(inp)
