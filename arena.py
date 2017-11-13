''' arena.py - Where ML and AI bots go to face off '''
from log import logger
import logging
import evaluation as ev
from random import choice
from models import test_models
from itertools import count
from models.abstract_models import EvolutionaryMLModel

_log = logger.get('arena', console_logging=True, level=logging.INFO)
LISTEN_TO_EVAL_LOG = False
EVAL_LOG_LEVEL = logging.INFO

# This outputs the evaluation log to your console
if LISTEN_TO_EVAL_LOG:
    console = logging.StreamHandler()
    console.setLevel(EVAL_LOG_LEVEL)
    ev._log.addHandler(console)


class Arena:
    MODEL_ID = 'model number'
    MODEL_POOL = [
        test_models.ZeroModel,
        test_models.RandomModel,
        test_models.RandomStaticModel,
    ]

    def __init__(self, model_pool=MODEL_POOL, n_models=100):
        self.model_id = Arena.MODEL_ID
        self.model_pool = model_pool
        self.model_gen = Arena.ModelGenerator(self)
        self.models = self.gen_new_models(n_models)
        self.n_tourneys = 0
        self.scores = []

    class ModelGenerator:

        def __init__(self, arena):
            self.arena = arena
            self.model_pool = self.arena.model_pool
            self.mdl_no = count()

        def __next__(self):
            mdl = choice(self.model_pool)()
            setattr(mdl, self.arena.model_id, self.mdl_no.__next__())
            return mdl

        def __iter__(self):
            return self

    def gen_model(self):
        return self.model_gen.__next__()

    def model_number(self, model):
        return getattr(model, self.model_id)

    # Set log_top to None to log all
    def compete(self, x_data, y_data, live_ratio=0.5, mutate_ratio=0.5, n_rounds=1, log_top=10,
                score_function=ev.DEFAULT_SCORE_FUNCTION, track_function=ev.DEFAULT_ERROR_FUNCTION):
        self.n_tourneys = self.n_tourneys + 1
        _log.info('')
        _log.info('Tournament ' + str(self.n_tourneys))
        for round_no in range(n_rounds):
            # Score each model
            score = ev.score_ml_models(self.models, x_data, y_data, score_function=score_function)
            error = ev.score_ml_models(self.models, x_data, y_data, score_function=track_function)
            self.models = sorted(self.models, key=lambda mdl: score[mdl], reverse=True)
            self.scores.append(score)
            # TODO: Panda-ize scoreboard
            _log.info('Round ' + str(round_no+1) + '/' + str(n_rounds))
            _log.info('{id}\t| model type\t\t| {sco:21}\t| {err:21}\t'
                      .format(id=self.model_id, sco=score_function.__name__, err=track_function.__name__))
            _log.info('----------------|-----------------------|-----------------------|-----------------------')
            for mdl in (self.models if log_top is None else self.models[:log_top]):
                _log.info(
                    str(self.model_number(mdl)).ljust(15) + ' | '
                    + str(mdl.name()).rjust(21) + ' | '
                    + str(score[mdl]).ljust(21) + ' | '
                    + str(error[mdl]).ljust(21)
                )
            # Kill and regenerate
            live_i = int(len(self.models)*live_ratio)
            regen = self.models[live_i:]
            _log.info('Regenerating ' + str(len(regen)) + ' models')
            _log.log(level=logging.INFO-1, msg='Regenerating models: ' + str([self.model_number(mdl) for mdl in regen]))
            for i, _ in enumerate(regen):
                self.models[live_i+i] = self.gen_model()
            _log.info('Next generation ready')
            _log.log(level=logging.INFO-1,
                     msg='Next generation models: ' + str([self.model_number(mdl) for mdl in self.models]))
            # Mutate any surviving evolutionary models
            live = self.models[:live_i]
            mutate_i = int(len(live)*mutate_ratio)
            mutate = live[mutate_i:]
            for mdl in mutate:
                if mdl is EvolutionaryMLModel:
                    mdl.mutate()
        _log.info(str(self.model_number(self.models[-1])+1) + ' models generated so far')

    def gen_new_models(self, n):
        '''
        Generate n new models
        :param n: The number of new models to generate
        :return: An iterable of the new models
        '''
        return [self.gen_model() for _ in range(n)]
