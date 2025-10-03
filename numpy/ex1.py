import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 8, 9, 10])

print(a[[1, 1, 1, 1, 1, 1]])

c = a.reshape(3,3)
print(c)
print(c[1,2]) 


# NP ARRAY

a1 = np.array([1, 2, 3, 4], 'str_')
print(a1, a1.dtype)

print(np.complex64(10))

print(np.int16(4.35))


a2 = np.array([1, 2, 1000, 5000])
print(a2)

a3 = np.array([[1, 2], [3, 4], [5, 6]])
print(a3)

print()

a4 = np.array(np.eye(3,3))
print(a4)

a5 = np.empty([4,4], 'int16')
print(a5)

a6 = np.eye(3)
print(a6)

a7 = np.identity(5)
print(a7) 

a8 = np.ones([5,5])
print(a8)

a9 = np.full([3,2], fill_value=-2)
print(a9)


# Matrix

print()
b1 = np.asmatrix('1 2;3 4')
print(b1)

print()
b2 = np.asmatrix([(1,2,3), (4,5,6)])
print(b2)

print()
b3 = np.diag([1,2,3])
print(b3)


print()
b3 = np.diag([[1,2,3], [4,5,6], [7,8,9]])
print(b3)

print()
b4 = np.diagflat([[1,2,3], [4,5,6], [7,8,9]])
print(b4)

print()
b4 = np.tri(3)
print(b4)


print()
b5 = np.asmatrix([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(np.tril(b5))
print(b5)

print()
b6 = np.asmatrix([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(np.triu(b6))


print()
print(np.vander([1, 2, 3]))

# Sequence

print()
c1 = np.arange(5)
c2 = np.arange(1, 5)
c3 = np.arange(1, 5, 0.5)
c4 = np.arange(1, np.pi, 0.1)
c5 = np.cos(np.arange(1, np.pi, 0.2))
print(c1, c2, c3, c4, c5, sep='\n')


print()
c1 = np.linspace(0, np.pi, 0)
c2 = np.linspace(0, np.pi, 1)
c3 = np.linspace(0, np.pi, 2)
c4 = np.linspace(0, np.pi, 3)

print(c1, c2, c3, c4, sep='\n', end='\n')

print()
c1 = np.logspace(0, 1, 4)
print(c1)

print()
c2 = np.geomspace(1, 4, 3)
print(c2)


# Form array

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.copy(a)
print(b)

def getRange(x, y):
    return 100*x + y

c = np.fromfunction(getRange, (3, 3))
print(c)

print()
a1 = np.fromiter("hello", 'U1')
print(a1)

def genRange(n):
    for i in range(n):
        yield i

a2 = np.fromiter(genRange(5), 'int16')
print(a2)

a3 = np.fromstring("1 2 3 4 5", "int16", sep=' ')
print(a3)

# WORK WITH NUMPY ARRAY PROPERTIES

a = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
a.dtype = np.int8()
print(a, a.dtype, a.size, a.itemsize, a.size*a.itemsize, sep='\n')


b = np.ones((3,4,5))
print(b)
print(f"b.ndim = {b.ndim}, b.shape = {b.shape}", end='\n\n')
b.shape = 60
b.shape = (4,15)
print(b, end='\n\n')


d = b.T
print(d)

a = np.array([1,2,3,4,5,6])
b = a.view() # copy view ONLY!

print()
a.shape = (2,3)
print(b)
print(a) 

b = np.array(a, copy=True) # deep copy
b = a.copy() # deep copy
