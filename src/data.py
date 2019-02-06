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

def random_data(amount, minimum, maximum):
        return np.random.randint(minimum, maximum+1, size=(amount, 2))


def linear_noise(amount, slope, minimum, maximum, noise):
    x = np.empty(amount)
    y = np.empty(amount)

    for i in range(0, amount):
        if i == 0:
            y[i] = minimum
            x[i] = i
        else:
            x[i] = i

            direction = np.random.random_integers(0, 2)

            if direction == 0:
                y[i] = y[0] + slope*x[i] + noise
            elif direction == 1:
                y[i] = y[0] + slope*x[i] - noise
            else:
                y[i] = y[0] + slope*x[i]

            if y[i] > maximum:
                y[i] = maximum

    return np.array((x, y)).T
