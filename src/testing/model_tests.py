from models import abstract_models, test_models
from numpy.random import uniform
from os import remove
from uuid import uuid4


def test_model_serialization(model_type=test_models.ZeroModel):

    saved_model = model_type()

    x_data = uniform(0, 1, (100, 1))
    y_data = uniform(0, 1, (100, 1))

    for (x, y) in zip(x_data, y_data):
        saved_model.learn(x, y)
    save_file = 'mdl_serial_test_' + str(uuid4())
    saved_model.save(save_file)
    loaded_model = abstract_models.Model.load(save_file)
    remove(save_file)
    if not saved_model == loaded_model:
        raise Exception('Model changed during serialization and deserialization process')
