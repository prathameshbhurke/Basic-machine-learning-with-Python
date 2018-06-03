cube = lambda x: pow(x, 3)  # complete the lambda function

def fibonacci(n):
    y = 2
    s = []
    if y >= 2:
        s.append(0)
        s.append(1)

    for y in range(2, n + 1):
        s.append(s[y - 2] + s[y - 1])

    return s[0:n]
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))