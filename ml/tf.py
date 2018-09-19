import numpy as np

print(np.__version__)

np.array([1,2,3])

a = np.zeros((3,2),dtype=int,order='F')

print(a)


a = np.arange(0,60,5)
a = a.reshape(3,4)

print(a)

for x in np.nditer(a):
    print (x),
