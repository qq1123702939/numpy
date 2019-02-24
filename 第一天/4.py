import numpy as np
a = np.array([10,20,30,40])
b = np.arange(4)

c = a**2

d = 10*np.tan(a)
print(a,b)
print('c',c)
print('d',d)

print('b',b)
print(b==3)


e = np.array([[1,1],
            [2,3]])
f = np.arange(4).reshape(2,2)

print('e',e)
print('f',f)

g = e*f
h = np.dot(e,f)
h_2 = e.dot(f) 


print('g',g)
print('h',h)
print('h_2',h_2)
j = np.random.random((2,4))
print('j',j)

print('sum',np.sum(j,axis=1))
print('min',np.min(j,axis=0))
print('max',np.max(j,axis=1))

