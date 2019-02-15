import numpy as np


def random_data(amount, minimum, maximum):
    if minimum >= maximum:
            raise ValueError("Minimum must be less than maximum")

    return (maximum - minimum) * np.random.rand(amount, 2) + minimum


def linear_noise(amount, slope, y_int):
    x = np.empty(amount)
    y = np.empty(amount)
    noise = 2 * np.random.rand(amount) - 1

    for i in range(0, amount):
        if i == 0:
            y[i] = y_int
            x[i] = i
        else:
            x[i] = i

            y[i] = y_int + slope*x[i] + noise[i]

    return np.array((x, y)).T
