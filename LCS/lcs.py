def LCS(s1, s2):
    m = len(s1)
    n = len(s2)
    # An (m+1) times (n+1) matrix
    C = [[0] * (n+1) for i in range(m+1)]
    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j]:
                C[i+1][j+1] = C[i][j] + 1
            else:
                C[i+1][j+1] = max(C[i+1][j], C[i][j+1])
    # return the length of LCS
    # return C[m][n]

    # derive the actual LCS
    lcs = ''
    i = m
    j = n
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            lcs += s1[i-1]
            i -= 1
            j -= 1
        elif C[i-1][j] >= C[i][j-1]:
            i -= 1
        else:
            j -= 1
    return lcs[::-1]
