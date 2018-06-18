a = [1,1,1,1,1,1,2,2,3,4,5,6,6,7,7,1,23,45,23,121,42]
a = list(set(a))
n = 9
arr = []

for i in a:
    if i >= n:
        continue
    else:
        arr.append(i)

l = len(arr)
j = l -1
i = 0
flag = 0

while i <= (l-1) and j >= 0:
    if arr[i]+arr[j] == n:
        print(arr[i],arr[j])
        flag = 1
        break
    elif arr[i]+arr[j] > n:
        i = i+1
        j = j -1
        #print('2nd')
    else:
        i = i +1
        #print('3rd')
if flag == 0:
    print("2 numbers in give list do not sum to n")
