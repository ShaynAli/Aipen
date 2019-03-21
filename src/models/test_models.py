""" test_models.py Simple models for testing """
import numpy as np
from models.abstract_models import MLModel


class ZeroModel(MLModel):
    """
    Always predicts zeros.
    Learns the shape of the output after each call to .learn(x, y)
    When .predict(x) is called an array of zeros is returned, it has the same number of rows as x, with all other
    dimensions based on the learned shape of y.
    """

    _DEFAULT_PREDICTION = np.zeros([])

    def __init__(self):
        super(ZeroModel, self).__init__()
        self.y_shape = None

    def learn(self, x, y):
        self.y_shape = y.shape

    def predict(self, x):
        if self.y_shape is None:  # No output shape has been learned
            return ZeroModel._DEFAULT_PREDICTION
        return np.zeros(self.y_shape)


class RandomModel(MLModel):
    """
    Predicts randomly, tries to have predictions fall within the possible output range.
    """
    from random import uniform

    DEFAULT_RANGE = [0, 1]
    DEFAULT_DISTRIBUTION = uniform

    def __init__(self, prediction_range=DEFAULT_RANGE, distribution=DEFAULT_DISTRIBUTION):
        super(RandomModel, self).__init__()
        self.z_mdl = ZeroModel()  # Zero model for shape
        self.prediction_range = prediction_range
        self.distribution = distribution

    def learn(self, x, y):
        self.z_mdl.learn(x, y)
        self.prediction_range[0] = min(np.min(y), self.prediction_range[0])
        self.prediction_range[1] = max(np.max(y), self.prediction_range[1])

    def predict(self, x):
        prediction = self.z_mdl.predict(x)
        if len(prediction) > 0:
            prediction[:] = [self.distribution(*self.prediction_range) for _ in prediction]
        return prediction


class RandomStaticModel(RandomModel):

    def __init__(self):
        super(RandomStaticModel, self).__init__()
        self.prediction = None

    def learn(self, x, y):
        super(RandomStaticModel, self).learn(x, y)

    def predict(self, x):
        if self.prediction is None:
            self.prediction = super(RandomStaticModel, self).predict(x)
        return self.prediction