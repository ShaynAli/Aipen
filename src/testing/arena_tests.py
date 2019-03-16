# TODO: Add use of argv to parameterize
from arena.arena import Arena
from data import test_models
from numpy.random import uniform


def run_test_arena(n_models=10, n_tournaments=10, n_rows=10,
                   n_x=3, min_x=0, max_x=1,
                   n_y=2, min_y=1, max_y=1):

    x_data = uniform(min_x, max_x, (n_rows, n_x))
    y_data = uniform(min_y, max_y, (n_rows, n_y))

    test_arena = Arena(
        n_models=n_models,
        model_pool=[
            test_models.RandomStaticModel,
            test_models.RandomModel,
            test_models.ZeroModel
        ])

    for _ in range(n_tournaments):
        test_arena.compete(x_data, y_data)

