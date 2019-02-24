import numpy as np
A = np.array([1,1,1])
B = np.array([2,2,2])

print(np.vstack((A,B)))

C = np.vstack((A,B))
print(A.shape,C.shape)

D = np.hstack((A,B))
print(D)
print(A.shape,D.shape)
print('------------np.newaxis-----------------')

print(A[np.newaxis,:])

print(A[np.newaxis,:].shape)

print(A[:,np.newaxis])

print(A[:,np.newaxis].shape)


print('------------综合-----------------')
A = np.array([1,1,1])[:,np.newaxis]
B = np.array([2,2,2])[:,np.newaxis]

E = np.vstack((A,B))
F = np.hstack((A,B))
print(F)
print(E)
print(F.shape,E.shape)

print('------------np.concatenate-----------------')
G = np.concatenate((A,B,B,A),axis=1)
print(G)
