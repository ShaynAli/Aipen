''' arena.py - Where ML and AI bots go to face off '''
from log import logger
import evaluation as ev
from random import choice
from models import test_models
import numpy as np
import pandas as pd

logging = logger.Log('arena', console_logging=True)


class Arena:
    MODEL_NO_STR = 'number'
    MODEL_POOL = [
        test_models.ZeroModel,
        test_models.RandomModel,
    ]

    def __init__(self, model_pool=MODEL_POOL, n=100):
        self.model_no = 0
        self.model_pool = model_pool
        self.models = self.gen_new_models(n)
        self.scores = None

    def compete(self, x_data, y_data, live_ratio=0.5, mutate_ratio=0.5):
        self.scores = ev.score_ml_models(self.models, x_data, y_data)
        # n_live = int(len(self.scores) * live_ratio)
        # kill = self.scores[n_live:]

    def gen_new_models(self, n):
        '''
        Generate n new models
        :param n: The number of new models to generate
        :return: An iterable of the new models
        '''
        models = []
        for i in range(n):
            model = choice(self.model_pool)
            models.append(model)
            setattr(model, Arena.MODEL_NO_STR, self.model_no)
            self.model_no = self.model_no + 1
        return models
