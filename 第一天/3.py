import numpy as np

a = np.array( [ [1,2,3],
                [2,3,4]] , dtype =np.int64 )

print('a.dtype',a.dtype)

b = np.array( [ [1,2,3],
                [2,3,4]] , dtype = np.float)

print('b.dtype',b.dtype)

c = np.ones((3,4),dtype=np.int)

print('c',c)

d = np.empty((3,4))

print('d',d)

e = np.arange(10,20,2)

print('e',e)

f = np.arange(12).reshape(4,3)

print('f',f)


g = np.linspace(1,10,6)

print('g',g)

h = np.linspace(1,10,6).reshape(2,3)

print('h',h)
