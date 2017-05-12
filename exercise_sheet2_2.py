import numpy as np
import functools
import math



np.set_printoptions(precision=3)


x = np.array([[1.0, 2, 4],
              [1.0,1, 0.5],
              [1.0,0.5, 1.5],
              [1.0,0, 0.5]])

w = np.array([0.0, 1.0, -1.0])

trouble = True

inc = 0.25

yh = 0
y = 0

steps = 0

while trouble:
    trouble = False
    for i in range(0, 4):
        if i < 2:
            y = 1
        else:
            y = -1
        yhtemp = x[i][0] * w[0] + x[i][1] * w[1] + x[i][2] * w[2]
        yh = np.sign(yhtemp)
        if y -yh != 0:
            steps += 1
            trouble = True
            print("Problem with: w:" + str(w))
            print("x: " + str(x[i]))
            for j in range(0, 3):
                w_old = w[j]
                w[j] = w[j] + inc * y * x[i][j]
                print("Fitting: old w" + str(j) + " : " + str(w_old) + " to w: " + str(w) + " for x: " + str(x[i]))

        else:
            print("No problem for: w: " + str(w))
            print("x: " + str(x[i]))

print("number of steps taken: " + str(steps))
print("end weights: " + str(w))
