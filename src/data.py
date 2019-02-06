import numpy as np
# n,p=10,0.5
# s=np.random.binomial(n,p,1000)
# print(s)

# import matplotlib.pyplot as plt
# import numpy as np
# n,p=10,0.5
# X=np.random.binomial(n,p,1000)
# plt.show()

import numpy as np


def randomDataGen(minVar,maxVar):
    amount=None


    x = np.random.randint(minVar,maxVar,size=(10,10))
    return x


def returnSlope(minX,maxX,minY,maxY):
    m=((maxY-minY)/(maxX-minX))
    return m

def intercept(minX,maxX,minY,maxY):
    m=returnSlope(minX,maxX,minY,maxY)
    q=minY-m*minX
    return q
def getLinearEquation(minX,maxX,minY,maxY,size,noise):
    m=returnSlope(minX,maxX,minY,maxY)
    q=intercept(minX,maxX,minY,maxY)
    x=np.empty(size)
    y = np.empty(size)
    for i in range(0,size):
        x[i]=i
        y[i]=m*i+q+np.random.randint(0,noise+1)

    return np.array((x,y)).T





print(randomDataGen(5,10))
print(returnSlope(2,3,4,5))
print(intercept(2,3,4,5))
print(getLinearEquation(2,3,4,5,10,5))




