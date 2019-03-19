""" arena.py - Where ML and AI bots go to face off """
from itertools import count
from random import choice
import evaluation
from utilities import partition_indices


class Arena:
    MODEL_ID_FIELD = 'model number'

    def __init__(self, model_pool, n_models=10):
        self.mdl_id_field = Arena.MODEL_ID_FIELD
        self.model_pool = model_pool
        self.model_gen = Arena.ModelGenerator(self)
        self.models = self.gen_new_models(n_models)
        self.scores = []

    def gen_model(self):
        return self.model_gen.__next__()

    def model_number(self, model):
        return getattr(model, self.mdl_id_field)

    def compete(self, x_data, y_data, live_ratio=0.5, score_function=evaluation.DEFAULT_SCORE_FUNCTION):
        print('Scoring models')
        score = evaluation.score_ml_models(self.models, x_data, y_data, score_function=score_function)
        self.models = sorted(self.models, key=lambda mdl: score[mdl], reverse=True)
        self.scores.append(score)
        _, kill_start, kill_end = partition_indices(self.models, live_ratio)
        print('Killing and regenerating models')
        self.models[kill_start:kill_end] = self.gen_new_models(kill_end - kill_start)

    def gen_new_models(self, n):
        """
        Generate n new models
        :param n: The number of new models to generate
        :return: A list of the new models
        """
        return [self.gen_model() for _ in range(n)]

    class ModelGenerator:

        def __init__(self, arena):
            self.arena = arena
            self.model_pool = self.arena.model_pool
            self.mdl_id_field = arena.mdl_id_field
            self.mdl_no = count()

        def __next__(self):
            mdl = choice(self.model_pool)()
            setattr(mdl, self.mdl_id_field, self.mdl_no.__next__())
            return mdl

        def __iter__(self):
            return self


class MachineLearningArena:

    def __init__(self, model_pool, n_models_per_generation=10):
        pass
