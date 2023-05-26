n = int(input())

m1 = 0
m2 = 1
i = 2
while m2 <= n:
    if m2 == n:
        print(i)
        break
    m1, m2 = m2, m1 + m2
    i += 1
else:
    print(-1)