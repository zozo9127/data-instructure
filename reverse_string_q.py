def r_q(s):
    n = len(s)
    for i in range (n // 2):
        s[n-1-i] , s[i] = s[i] , s[n-1-i]
    return s