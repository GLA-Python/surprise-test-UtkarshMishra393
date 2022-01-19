def check(a):
    x = []
    y = []
    z = []
    v = []
    w = []
    for i in range(len(a)-1):
        x.append(a[i])
    for i in range(1, len(a)):
        y.append(a[i])
    for i in range(len(x)):
        diff = y[i] - x[i]
        z.append(diff**2)
    for i in range(len(z)-1):
        v.append(z[i])
    
    for i in range(1, len(z)):
        w.append(z[i])

    for i in range(len(v)):
        if w[i]<=v[i]:
            return False
    return True

n = list(map(int, input().split()))
print(check(n))
