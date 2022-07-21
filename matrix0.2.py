import numpy as np
A = np.array([[2,1,2],
    [1,4,4],
    [3,3,1]])
B = np.array([1,0,0])
print("Solution:\n ",np.linalg.solve(A,B))
