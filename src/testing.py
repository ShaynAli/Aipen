# TODO: Add use of argv to parameterize
from arena import Arena
from models import test_models
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


def test_model_serialization():
    from models import test_models
    from numpy.random import uniform, randint
    from os import remove

    r_m = test_models.RandomStaticModel()

    x_data = uniform(0, 1, (100, 1))
    y_data = uniform(0, 1, (100, 1))

    for (x, y) in zip(x_data, y_data):
        r_m.learn(x, y)
    save_file = 'mdl_serial_test_' + str(randint(0, 1000))
    r_m.save(save_file)
    before_save = r_m.predict(x_data[0])
    test_models.RandomStaticModel.load(save_file)
    after_save = r_m.predict(x_data[0])
    remove(save_file)
    assert before_save == after_save


run_test_arena(n_models=10)
