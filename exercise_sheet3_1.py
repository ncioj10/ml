import numpy as np

xm = np.matrix([[1,3],[1,4],[1,5],[1,6],[1,7],[1,8]]).astype(float)
ym = np.matrix([150,155,150,170,160,175]).astype(float).T
wm = np.matrix([0,0])

running = True
inc = 0.001



m, c = np.linalg.lstsq(xm, ym)[0]
print (m, c)
counter = 0

while running:
    weights = np.matrix([0, 0])
    counter +=1
    running = False
    for x,y in zip(xm,ym):
        yh = x * wm.T
        diff = (y - yh)
        weights = weights + diff[0][0] * x

        if diff[0][0] != 0.0  :
            running = True

    wm = wm + weights * inc
    if counter > 100000:
        break



print(wm)






