import numpy as np
from arena import Arena
from sys import argv
from models import test_models
import evaluation as ev

params = {'n_rows': 50, 'n_models': 10, 'n_tournaments': 100, 'live_ratio': 0.5}
if len(argv) > 1:
    print(argv)
    for i in range(int(len(argv)/2)):
        params[argv[2*i+1]] = float(argv[2*i+2])

n_x = 1; min_x = 0; max_x = 1
n_y = 1; min_y = 0; max_y = 1
n_rows = int(params['n_rows'])
n_models = int(params['n_models'])
n_tournaments = int(params['n_tournaments'])
live_ratio = params['live_ratio']

# x_data = np.zeros((n_rows, n_x))
# y_data = np.zeros((n_rows, n_y))

x_data = np.random.uniform(min_x, max_x, (n_rows, n_x))
y_data = np.random.uniform(min_y, max_y, (n_rows, n_y))

arena_1 = Arena(n_models=n_models, model_pool=[test_models.RandomStaticModel])
arena_2 = Arena(n_models=n_models, model_pool=[test_models.RandomStaticModel])
for i in range(n_tournaments):
    arena_1.compete(x_data, y_data, live_ratio=live_ratio, score_function=ev.inverse_norm_err)
    arena_2.compete(x_data, y_data, live_ratio=live_ratio, score_function=ev.accuracy)


def assert_no_duplicates(iterable):
    s = set()
    for e in iterable:
        assert e not in s
        s.add(e)
