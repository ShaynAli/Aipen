import numpy as np
import pickle


class Data:
    def __init__(self):
        self.data = np.empty([2, 2])
        self.id = np.empty.__hash__()

    def set_random(self, amount, minimum, maximum):
        self.data = random_data(amount, minimum, maximum)
        self.id = self.__hash__()

    def set_linear(self, amount, slope, y_int):
        self.data = linear_noise(amount, slope, y_int)
        self.id = self.__hash__()

    def set_data(self, data):
        self.data = data
        self.id = self.__hash__()

    def save_data(self):
        pickle_out = open("data.pickle", "wb")
        pickle.dump(self.data, pickle_out)
        pickle_out.close()

        pickle_out = open("id.pickle", "wb")
        pickle.dump(self.id, pickle_out)
        pickle_out.close()

    def get_data(self):
        pickle_in = open("data.pickle", "rb")
        self.data = pickle.load(pickle_in)
        pickle_in.close()

        pickle_in = open("id.pickle", "rb")
        self.id = pickle.load(pickle_in)
        pickle_in.close()


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

