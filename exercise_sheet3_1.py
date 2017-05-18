import numpy as np

xm = np.matrix([[1,3,9],[1,4,16],[1,5,25],[1,6,36],[1,7,49],[1,8,64]]).astype(float)
ym = np.matrix([150,155,150,170,160,175]).astype(float).T
wm = np.matrix([0,0,0])

running = True
inc = 0.0001



wl = np.linalg.lstsq(xm, ym)[0]
print (wl)
counter = 0
weights = np.matrix([0, 0, 0]).astype(float)
sum = 0
for x,y in zip(xm,ym):
    d = (x * wl)
    sum = sum+ ((y- d) **2)
print(sum)
while running:
    weights = np.matrix([0, 0,0]).astype(float)
    counter +=1
    running = False
    for x,y in zip(xm,ym):
        yh = x * wm.T
        diff = (y - yh)
        weights = weights + diff * x
        running  = True




    wm = wm + weights * inc
    if counter > 10000000:
        break




print(wm)






