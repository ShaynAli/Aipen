''' evaluation.py - Evaluates AI and ML models '''

from warnings import warn
import numpy as np
from math import ceil

# For ML models

EVAL_BATCH_SIZE = 1
N_EPOCHS = 1

def eval_prediction(x, y_predicted, y_actual):
    return 0


# def eval_predictions(x_data, y_predicted_data, y_actual_data):
#     pass


def eval_ml_model(model, x_data, y_data, batch_size=EVAL_BATCH_SIZE, n_epochs=N_EPOCHS):
    '''
    
    :param model: 
    :param x_data: 
    :param y_data: 
    :param batch_size: 
    :param n_epochs: 
    :return: 
    '''

    n_x = x_data.shape[0]  # Number of x entries
    n_y = y_data.shape[0]  # Number of y entries
    if n_x != n_y:
        warn('x and y data do not have the same number of entries')

    max_i = min(n_x, n_y)
    n_batches = int(ceil(max_i / batch_size))
    scores = np.zeros((n_epochs, n_batches))

    for epoch_i in range(n_epochs):
        print('\tEpoch ' + str(epoch_i))
        data_i = 0
        # Go through each batch, test, then train
        for batch_i in range(n_batches):
            print('\t\tBatch ' + str(batch_i))
            max_batch_i = min(data_i + batch_size, max_i)
            # Test
            for i in range(data_i, max_batch_i):
                print('\t\t\tTesting ' + str(i))
                x = x_data[i]
                y = y_data[i]
                scores[epoch_i][batch_i] = eval_prediction(x, model.predict(x), y)
            # Train
            for i in range(data_i, max_batch_i):
                print('\t\t\tTraining ' + str(i))
                x = x_data[i]
                y = y_data[i]
                model.learn(x, y)
            data_i = data_i + batch_size


def eval_ml_models(models, x_data, y_data):
    perf = {}  # Begin with empty dict, then fill
    for mdl in models:
        perf[mdl] = eval_ml_model(mdl, x_data, y_data)
    return perf


# For AI models

# TODO
