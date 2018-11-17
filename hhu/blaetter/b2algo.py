def mystery(n):
    r = 0
    for i in range(n+1):
        for j in range(i+1, n + 1):
            for k in range(i+1, j + 1):
                r += 1
    return n


for i in range(20):
    print(mystery(i))