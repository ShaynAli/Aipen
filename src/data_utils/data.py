import numpy as np
from utilities import Serializable


class Data(Serializable):
    def __init__(self, data=np.empty(0)):
        self._data = data
        self.shape = data.shape

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_data):
        self._data = new_data


def random_data(amount, minimum, maximum):
    return (maximum - minimum) * np.random.rand(amount, 2) + minimum


def linear_noise_data(start, stop, n_samples=100, noise=1):
    linear = np.linspace(start, stop, n_samples)
    noise = noise * 2 * (np.random.rand(n_samples) - 0.5)
    return linear + noise


def indexed_linear_noise_data(start, stop, n_samples=100, noise=1):
    return np.vstack((np.linspace(start, stop, n_samples), linear_noise_data(start, stop, n_samples, noise)))
