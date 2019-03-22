from activities.stock_prediction.stock_prediction import FrankfurtStockPrediction
import numpy as np
from keras import Sequential
from keras.layers import Dense, Activation
from random import randint


class RandomRangePredictor(FrankfurtStockPrediction.Model):

    def __init__(self, activity):
        super().__init__(activity)
        self.min = 0
        self.max = 1

    def train(self, x, y):
        self.min = min(self.min, np.min(y))
        self.max = max(self.max, np.max(y))

    def predict(self, x):
        return np.random.uniform(size=(self.y_shape[0], x.shape[1]))

    @staticmethod
    def description():
        return '''Predicts within a random range. The max and min of the range are updated based on y data.'''


class MeanPredictor(FrankfurtStockPrediction.Model):

    def __init__(self, activity):
        super().__init__(activity)

    def train(self, x, y):
        pass

    def predict(self, x):
        return np.full(shape=(self.y_shape[0], x.shape[1]), fill_value=np.mean(x))

    @staticmethod
    def description():
        return '''Predicts that every stock will have the same mean price overall.'''


class MeanRowPredictor(FrankfurtStockPrediction.Model):

    def __init__(self, activity):
        super().__init__(activity)

    def train(self, x, y):
        pass

    def predict(self, x):
        n_y_cols = self.y_shape[1]
        prediction = np.empty(shape=self.y_shape)
        for row_i in range(x.shape[0]):
            row_mean = np.mean(x[row_i, :])
            prediction[:, row_i] = [row_mean] * n_y_cols
        return prediction

    @staticmethod
    def description():
        return '''Predicts that every stock will have the same mean price at every time interval.'''


class ShallowNeuralNetworkPredictor(FrankfurtStockPrediction.Model):

    def __init__(self, activity):
        super().__init__(activity)
        self.neural_network = Sequential([
            Dense(32, input_shape=(self.x_shape[1],)),
            Dense(self.y_shape[1])
        ])
        self.neural_network.compile(
            optimizer='nadam',
            loss='mse'
        )

    def train(self, x, y):
        self.neural_network.fit(x=x, y=y)

    def predict(self, x):
        return self.neural_network.predict(x)

    @staticmethod
    def description():
        return '''Uses a shallow, wide neural network.'''


class RandomDepthNeuralNetworkPredictor(FrankfurtStockPrediction.Model):

    def __init__(self, activity):
        super().__init__(activity)
        self.neural_network = Sequential([Dense(8, input_shape=(self.x_shape[1],))] +
                                         [Dense(8) for _ in range(randint(0, 8))] +
                                         [Dense(self.y_shape[1])])
        self.neural_network.compile(
            optimizer='nadam',
            loss='mse'
        )

    def train(self, x, y):
        self.neural_network.fit(x=x, y=y)

    def predict(self, x):
        return self.neural_network.predict(x)

    @staticmethod
    def description():
        return '''Creates a neural network of depth from 2-10.'''
