import numpy as np
from arena import Arena

n_rows = 1000
n_x = 1; min_x = 0; max_x = 1
n_y = 1; min_y = 0; max_y = 1
n_tournaments = 1000

# x_data = np.zeros((n_rows, n_x))
# y_data = np.zeros((n_rows, n_y))

x_data = np.random.uniform(min_x, max_x, (n_rows, n_x))
y_data = np.random.uniform(min_y, max_y, (n_rows, n_y))

arena = Arena(n_models=20)
for i in range(n_tournaments):
    arena.compete(x_data, y_data)


def assert_no_duplicates(iterable):
    s = set()
    for e in iterable:
        assert e not in s
        s.add(e)
