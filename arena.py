''' arena.py - Where ML and AI bots go to face off '''
import numpy as np
import pandas as pd
import evaluation as ev
from collections import OrderedDict

class Arena():

    def __init__(self, models):
        self.models = models
        self.scoreboard = OrderedDict()

    def compete(self, x_data, y_data, kill_ratio=0.5, mutate_ratio=0.5):
        scores = ev.score_ml_models(self.models, x_data, y_data)


    def gen_new_models(self, n):
        '''
        Generate n new models
        :param n: The number of new models to generate
        :return: An iterable of the new models
        '''
        pass
