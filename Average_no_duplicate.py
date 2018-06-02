

def average1(array):
    #print(array)
    s = []
    avg = 0
    for x in array:
        if x not in s:
            s.append(x)
    avg = sum(s)/len(s)
    return avg
    # your code goes here

def average2(array):
    # print(array)
    avg = 0
    avg = sum(set(array)) / len(set(array))
    return avg

if __name__ == '__main__':
    n = input()
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)