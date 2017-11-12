''' evaluation.py - Evaluates AI and ML models '''

from warnings import warn
import numpy as np
from math import ceil
import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

# For ML models

EVAL_BATCH_SIZE = 1
N_EPOCHS = 1


def accuracy(predicted, actual, rounding=False):
    if predicted.shape != actual.shape:
        raise RuntimeError('Shape mismatch, predicted had shape {predicted_shape} while actual had shape {actual_shape}'
                           .format(predicted_shape=predicted.shape, actual_shape=actual.shape))
    if rounding:
        err = np.round(predicted) - actual
    else:
        err = predicted - actual
    abs_err = np.absolute(err)
    return 1 - np.mean(abs_err)


def score_prediction(x, y_predicted, y_actual, score=accuracy):
    return score(y_predicted, y_actual)


# def eval_predictions(x_data, y_predicted_data, y_actual_data):
#     pass


def score_ml_model(model, x_data, y_data, batch_size=EVAL_BATCH_SIZE, n_epochs=N_EPOCHS):
    # TODO
    '''
    
    First batch will be trained but not tested on, this allows the model to learn the shape of the input and output
    :param model: 
    :param x_data: 
    :param y_data: 
    :param batch_size: 
    :param n_epochs: 
    :param train_first: Whether 
    :return: 
    '''

    n_x = x_data.shape[0]  # Number of x entries
    n_y = y_data.shape[0]  # Number of y entries
    if n_x != n_y:
        warn('x and y data do not have the same number of entries')

    max_i = min(n_x, n_y)
    n_batches = int(ceil(max_i / batch_size))
    scores = np.zeros((n_epochs, n_batches))

    # Train one batch for shape
    for i in range(0, min(batch_size, max_i)):
        logging.debug('\t\tBatch 0')
        logging.debug('\t\t\tTraining for shape ' + str(i))
        x = x_data[i]
        y = y_data[i]
        model.learn(x, y)

    for epoch_i in range(n_epochs):
        logging.debug('\tEpoch ' + str(epoch_i))
        data_i = batch_size
        # Go through each batch, test, then train
        for batch_i in range(1, n_batches):
            logging.debug('\t\tBatch ' + str(batch_i))
            max_batch_i = min(data_i + batch_size, max_i)
            # Test
            for i in range(data_i, max_batch_i):
                logging.debug('\t\t\tTesting ' + str(i))
                x = x_data[i]
                y = y_data[i]
                scores[epoch_i][batch_i] = score_prediction(x, model.predict(x), y)
            # Train
            for i in range(data_i, max_batch_i):
                logging.debug('\t\t\tTraining ' + str(i))
                x = x_data[i]
                y = y_data[i]
                model.learn(x, y)
            data_i = data_i + batch_size
    return scores


def score_ml_models(models, x_data, y_data):
    perf = {}  # Begin with empty dict, then fill
    for mdl in models:
        perf[mdl] = score_ml_model(mdl, x_data, y_data)
    return perf


# For AI models

# TODO
