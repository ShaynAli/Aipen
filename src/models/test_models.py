''' test_models.py Simple models for testing '''
import numpy as np
from models.abstract_models import MLModel


class ZeroModel(MLModel):

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

    def properties(self):
        pass

    def summary(self):
        return '''
            ZeroModel\n
            \tAlways predicts zeros\n
            \tLearns the shape of the output after each call to .learn(x, y)\n
            \tWhen .predict(x) is called an array of zeros is returned, it has the same number of rows as x, with all\n
            \tother dimensions based on the learned shape of y
            '''


class RandomModel(MLModel):
    from random import uniform

    _DEFAULT_RANGE = [0, 1]
    # _DEFAULT_LEARN_RANGES = True  # Whether to learn the range of each output - TODO: Implement
    _DEFAULT_DISTRIBUTION = uniform

    def __init__(self, range=_DEFAULT_RANGE, distribution=_DEFAULT_DISTRIBUTION):
        super(RandomModel, self).__init__()
        self.z_mdl = ZeroModel()  # Zero model for shape
        self.range = range
        self.distribution = distribution

    def learn(self, x, y):
        self.z_mdl.learn(x, y)
        self.range[0] = min(np.min(y), self.range[0])  # Update min
        self.range[1] = max(np.max(y), self.range[1])  # Update max

    def predict(self, x):
        prediction = self.z_mdl.predict(x)
        if len(prediction) > 0:
            prediction[:] = [self.distribution(*self.range) for _ in prediction]
        return prediction

    def properties(self):  # TODO
        pass

    def summary(self):
        return '''
            RandomModel\n
            \tPredicts randomly, tried to have predictions fall within the possible output range
            '''


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

    def properties(self):  # TODO
        pass

    # TODO: summary()
