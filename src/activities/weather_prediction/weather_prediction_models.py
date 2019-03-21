from activities.weather_prediction.weather_prediction import HungaryWeatherPrediction
import numpy as np
import pdb


class RandomRangePredictor(HungaryWeatherPrediction.Model):

    def __init__(self, activity):
        super().__init__(activity)
        self.min = 0
        self.max = 1

    def train(self, x, y):
        self.min = np.min(y)
        self.max = np.max(y)

    def predict(self, x):
        return np.random.uniform(size=(self.y_shape[0], x.shape[1]))