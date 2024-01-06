def r(s):
    n = len(s)
    x = [None] * n
    for i in range (n):
        x[n - 1 - i] = s[i]
    return x