import numpy as np

A  = np.array([[1],[2],[3]])
print(A.shape[0])
B=np.array([[1],[2],[4]])
cross=np.cross(np.transpose(A),np.transpose(B))
print(cross)
print(cross.ndim)
print(A.ndim)

