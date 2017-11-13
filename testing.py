import numpy as np
from arena import Arena
from sys import argv
from models import test_models
import evaluation as ev

# TODO: Write data module (processing, generation), model auto-serialization, more models

params = {'n_rows': 10, 'n_models': 10, 'n_tournaments': 10, 'live_ratio': 0.5}
if len(argv) > 1:
    print(argv)
    for i in range(int(len(argv)/2)):
        params[argv[2*i+1]] = float(argv[2*i+2])

n_x = 1; min_x = -1; max_x = 1
n_y = 1; min_y = -1; max_y = 1
n_rows = int(params['n_rows'])
n_models = int(params['n_models'])
n_tournaments = int(params['n_tournaments'])
live_ratio = params['live_ratio']

# x_data = np.zeros((n_rows, n_x))
# y_data = np.zeros((n_rows, n_y))

x_data = np.random.uniform(min_x, max_x, (n_rows, n_x))
y_data = np.random.uniform(min_y, max_y, (n_rows, n_y))

_arena = Arena(n_models=n_models)
for i in range(n_tournaments):
    _arena.compete(x_data, y_data, live_ratio=live_ratio)


def assert_no_duplicates(iterable):
    s = set()
    for e in iterable:
        assert e not in s
        s.add(e)
