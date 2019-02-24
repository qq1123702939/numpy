import numpy as np
A = np.arange(3,15).reshape(3,4)



print(A)
print('索引位置')
print(np.argmax(A))
print(np.argmin(A))

print('平均值,')
print(A.mean())

print(np.median(A))

print('逐渐求和',np.cumsum(A))
print('累减')
print(np.diff(A))
print(np.nonzero(A))

print('------------')
B = np.arange(15,3,-1).reshape(3,4)
print(B)
print(np.sort(B))
print('转置')
print(B.T)
