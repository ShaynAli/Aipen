from models import abstract_models, test_models
from numpy.random import uniform
from os import remove
from uuid import uuid4


def test_model_serialization(model_type = test_models.RandomModel):
    # TODO: Improve, currently uses model predictions, should compare models directly
    # TODO: Add logging

    r_m = model_type()

    x_data = uniform(0, 1, (100, 1))
    y_data = uniform(0, 1, (100, 1))

    for (x, y) in zip(x_data, y_data):
        r_m.learn(x, y)
    save_file = 'mdl_serial_test_' + str(uuid4())
    r_m.save(save_file)
    before_save = r_m.predict(x_data[0])
    abstract_models.SerializableModel.load(save_file)
    after_save = r_m.predict(x_data[0])
    remove(save_file)
    assert before_save == after_save
