import numpy as np

import evaluation as ev
from models import test_models
from arena import Arena

z_mdls = []
r_mdls = []
for i in range(5):
    z_mdls.append(test_models.ZeroModel())
    r_mdls.append(test_models.RandomModel())
models = z_mdls + r_mdls

n_rows = 8
n_x = 3; min_x = 0; max_x = 1
n_y = 1; min_y = 0; max_y = 1

# x_data = np.zeros((n_rows, n_x))
# y_data = np.zeros((n_rows, n_y))

x_data = np.random.uniform(min_x, max_x, (n_rows, n_x))
y_data = np.random.uniform(min_y, max_y, (n_rows, n_y))

arena = Arena(models)
arena.compete(x_data, y_data)
