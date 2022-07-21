A = [[1,2,3],
    [8,5,4],
    [3,2,4]]
B = [[1,2],
    [2,3],
    [1,0]]
C = [[0,0],
    [0,0],
    [0,0]]

for i in range(0,len(C)):
    for j in range(0,len(C[0])):
        for k in range (0,len(B)):
                C[i][j] += A[i][k] * B[k][j]
for row in C:
    print(row)                                                                      