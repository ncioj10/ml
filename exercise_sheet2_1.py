import numpy as np

a_v = np.array([1,2,1])
b_v = np.array([2,2,1])

a = np.matrix([[1,2],
               [2,1],
               [1,1]])

b = np.matrix([[2,1],
               [1,2]])

c = np.matrix([[1,3],
               [0,1]])


# ecercise 2-1a
e1 = np.outer(a_v ,b_v)
print("atb: ")
print(e1)

e2 = np.outer(a_v,b_v)
print("abt:" )
print(e2)

e3 = a*c

print("AC: ")
print(e3)

e4 = c*a.transpose()
print("CAt:" )
print(e4)

e5 = a.transpose().dot(a_v)
print("Att:" )
print(e5)

e6 = a_v.transpose() * a

print("atA:")
print(e6)

# ecercise 2-1b

e7 = np.linalg.inv(b)
print("b-1:")
print(e7)
e8 = e7.dot(b)
i= np.identity(b.ndim)
if np.array_equal(e8, i):
    print("works")

# ecercise 2-1c

o = np.matrix([[0,1,0],
               [1,0,0],
               [0,0,1]])

product = np.dot(o,o.T)
cnt = np.count_nonzero(np.where(o >1))
if (cnt>0):
    print("non orthogonal")
else:
    np.fill_diagonal(product,0)
    if (product.any() == 0):
        print("orthonormal")
    else:
        print("non orthonormal")