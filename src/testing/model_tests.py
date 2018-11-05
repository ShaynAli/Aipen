from models import abstract_models, test_models
from numpy.random import uniform
from os import remove
from uuid import uuid4


def test_model_serialization(model_type = test_models.RandomStaticModel):
    # TODO: Fix, currently uses model predictions, should compare models directly
    # TODO: Add logging

    saved_model = model_type()

    x_data = uniform(0, 1, (100, 1))
    y_data = uniform(0, 1, (100, 1))

    for (x, y) in zip(x_data, y_data):
        saved_model.learn(x, y)
    save_file = 'mdl_serial_test_' + str(uuid4())
    saved_model.save(save_file)
    saved_model_prediction = saved_model.predict(x_data[0])
    loaded_model = abstract_models.SerializableModel.load(save_file)
    loaded_model_prediction = loaded_model.predict(x_data[0])
    remove(save_file)
    if saved_model_prediction != loaded_model_prediction:
        raise Exception('Model changed during serialization and deserialization process')
