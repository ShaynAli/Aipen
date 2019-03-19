import numpy as np
import pickle


class Data:
    def __init__(self, data=np.empty(0)):
        self.data = data
        self.shape = data.shape

    @property
    def data(self):
        return self.data

    @data.setter
    def data(self, new_data):
        self.data = new_data

    def save(self, file_name):
        with open(file_name, 'w') as file:
            pickle.dump(self, file)

    @staticmethod
    def load(file_name):
        with open(file_name, 'r') as file:
            return pickle.load(file)

    # def set_random(self, amount, minimum, maximum):
    #     self.data = random_data(amount, minimum, maximum)
    #     self.id = self.__hash__()
    #
    # def set_linear(self, amount, slope, y_int):
    #     self.data = linear_noise(amount, slope, y_int)
    #     self.id = self.__hash__()


def random_data(amount, minimum, maximum):
    return (maximum - minimum) * np.random.rand(amount, 2) + minimum


def linear_noise(start, stop, n_samples=100, noise=1):
    linear = np.linspace(start, stop, n_samples)
    noise = noise * 2 * (np.random.rand(n_samples) - 0.5)
    return linear + noise
