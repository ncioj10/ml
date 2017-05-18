import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.matrix([-5,7,3], dtype = float)

v = np.matrix([[5,4,4],[-3,-1,-2]], dtype = float).T
w = np.matrix([[5,-2],[-2,5]], dtype = float)


test = x *v
zh = sigmoid(test)
yh = w*zh.T


print(zh)
print(yh)