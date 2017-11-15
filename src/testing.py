from sys import argv
from arena import Arena
from models import test_models


def assert_no_duplicates(iterable):
    s = set()
    for e in iterable:
        assert e not in s
        s.add(e)


def run_test_arena(n_models=10, n_tournaments=10, n_rows=10,
                   n_x=3, min_x=0, max_x=1,
                   n_y=2, min_y=1, max_y=1):
    from numpy.random import uniform

    # x_data = np.zeros((n_rows, n_x))
    # y_data = np.zeros((n_rows, n_y))

    x_data = uniform(min_x, max_x, (n_rows, n_x))
    y_data = uniform(min_y, max_y, (n_rows, n_y))

    _arena = Arena(n_models=n_models, model_pool=[test_models.RandomStaticModel])
    for _ in range(n_tournaments):
        _arena.compete(x_data, y_data)


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


# Parse argv
params = {}
if len(argv) > 1:
    print(argv)
    for i in range(int(len(argv)/2)):
        params[argv[2*i+1]] = argv[2*i+2]

test_model_serialization()
run_test_arena()
