from activities.stock_prediction.stock_prediction import FrankfurtStockPrediction
import numpy as np
import pdb


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

    def parameters(self):
        return {
            'min': self.min,
            'max': self.max
        }
