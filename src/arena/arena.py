""" arena.py - Where ML and AI bots go to face off """
from itertools import count
from random import choice

import logger
from constants import LogNames
import evaluation
import models.test_models as test_models
from models.abstract_models import EvolutionaryModel

log = logger.log(LogNames.ARENA.value, level=logger.INFO)
LISTEN_TO_EVAL_LOG = False

# This outputs the evaluation log to your console
if LISTEN_TO_EVAL_LOG:
    logger.listen_to_log(LogNames.EVALUATION.value, logger.console(LogNames.ARENA.value))


class Arena:
    MODEL_ID_FIELD = 'model number'
    MODEL_POOL = [
        test_models.ZeroModel,
        test_models.RandomModel,
        test_models.RandomStaticModel,
    ]

    def __init__(self, model_pool=MODEL_POOL, n_models=100):
        self.mdl_id_field = Arena.MODEL_ID_FIELD  # Set id field name
        self.model_pool = model_pool
        self.model_gen = Arena.ModelGenerator(self)  # Set generator (requires model_pool to be set)
        # TODO: Add parameter and initialization of initial models
        self.models = self.gen_new_models(n_models)
        self.n_tourneys = 0
        self.scores = []

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

    def gen_model(self):
        return self.model_gen.__next__()

    def model_number(self, model):
        return getattr(model, self.mdl_id_field)

    # Set log_top to None to log all
    def compete(self, x_data, y_data, live_ratio=0.5, mutate_ratio=0.5, n_rounds=1, log_top=10,
                fitness_function=evaluation.DEFAULT_SCORE_FUNCTION, track=evaluation.DEFAULT_ERROR_FUNCTION):
        self.n_tourneys = self.n_tourneys + 1
        log.info('Tournament ' + str(self.n_tourneys))
        for round_no in range(n_rounds):
            # Score each model
            score = evaluation.score_ml_models(self.models, x_data, y_data, score_function=fitness_function)
            error = evaluation.score_ml_models(self.models, x_data, y_data, score_function=track)
            self.models = sorted(self.models, key=lambda mdl: score[mdl], reverse=True)
            self.scores.append(score)
            # TODO: Panda-ize scoreboard
            log.info('Round ' + str(round_no + 1) + '/' + str(n_rounds))
            log.info('{id}\t| model type\t\t| {sco:21}\t| {err:21}\t'
                     .format(id=self.mdl_id_field, sco=fitness_function.__name__, err=track.__name__))
            log.info('----------------|-----------------------|-----------------------|-----------------------')
            for mdl in (self.models if log_top is None else self.models[:log_top]):
                log.info(
                    str(self.model_number(mdl)).ljust(15) + ' | '
                    + str(mdl.__class__.__name__).rjust(21) + ' | '
                    + str(score[mdl]).ljust(21) + ' | '
                    + str(error[mdl]).ljust(21)
                )
            # Kill and regenerate
            live_i = int(len(self.models)*live_ratio)
            regen = self.models[live_i:]
            log.info('Regenerating ' + str(len(regen)) + ' models')
            log.info('Regenerating models: ' + str([self.model_number(mdl) for mdl in regen]))
            for i, _ in enumerate(regen):
                self.models[live_i+i] = self.gen_model()
            log.info('Next generation ready')
            log.info('Next generation models: ' + str([self.model_number(mdl) for mdl in self.models]))
            # Mutate any surviving evolutionary models
            live = self.models[:live_i]
            mutate_i = int(len(live)*mutate_ratio)
            mutate = live[mutate_i:]
            for mdl in mutate:
                if mdl is EvolutionaryModel:
                    mdl.mutate()
        log.info(str(self.model_number(self.models[-1]) + 1) + ' models generated so far')
        log.info('')

    def gen_new_models(self, n):
        """
        Generate n new models
        :param n: The number of new models to generate
        :return: An iterable of the new models
        """
        return [self.gen_model() for _ in range(n)]
