import numpy as np
A = np.arange(3,15)
print(A)
print(A[5])

A1 = np.arange(3,15).reshape(3,4)
print('A1',A1)
print(A1[2])

print('------二维索引-------')

print(A1[2,2])
print(A1[1,1:3])


print('------for循环打印-------')

A2 = np.arange(3,15).reshape(3,4)
print(A2)
for row in A2:
    print('1.',row)
for col in A2.T:
    print('2.',col)

print(A2.flatten())
for item in A.flat:
      print('item',item)
