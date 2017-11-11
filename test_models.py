''' test_models.py Simple models for testing '''

from abstract_models import MLModel, EvolutionaryMLModel
import numpy as np


class ZeroModel(MLModel):

    def __init__(self):
        super(ZeroModel, self).__init__()
        self.y_shape = None

    def learn(self, x, y):
        self.y_shape = y.shape

    def predict(self, x):
        if self.y_shape is None:  # No output shape has been learned
            return np.zeros(None)
        return np.zeros(x.shape[0:1] + self.y_shape[1:])

    def summary(self):
        return '''
            ZeroModel\n
            \tAlways predicts zeros\n
            \tLearns the shape of the output after each call to .learn(x, y)\n
            \tWhen .predict(x) is called an array of zeros is returned, it has the same number of rows as x, with all\n
            \tother dimensions based on the learned shape of y
            '''

