''' evaluation.py - Evaluates AI and ML models '''
from log import logger
import logging
from math import ceil
import numpy as np


# TODO Break apart ML and AI files into different modules

# Logging
_log = logger.get('evaluation')
EPOCH_LOG_LEVEL = logging.INFO - 1
BATCH_LOG_LEVEL = logging.INFO - 2
TEST_LOG_LEVEL = logging.INFO - 3
TEST_ELEMENT_LOG_LEVEL = logging.INFO - 4
TRAIN_LOG_LEVEL = logging.INFO - 3
TRAIN_ELEMENT_LOG_LEVEL = logging.INFO - 4
ELEMENT_LOG_LEVEL = logging.INFO - 5

# For ML models
EVAL_BATCH_SIZE = 5
N_EPOCHS = 1
N_PRE_TRAINING = 1


def gaussian(x, a=1, mu=0, sigma=1):
    return a*np.exp(-(((x - mu)/(2.*sigma))**2))


def simple_gaussian(x):
    return np.exp(-(x**2))


# Error functions


def absolute_error(predicted, actual):
    return np.absolute(predicted - actual)


def mean_abs_error(predicted, actual):
    return np.mean(absolute_error(predicted, actual))


def rms_error(predicted, actual):
    return np.sqrt(np.mean((predicted - actual)**2))


def norm_err(predicted, actual):
    return np.linalg.norm(predicted - actual)


def mean_pct_error(predicted, actual):
    return np.mean(np.absolute((predicted-actual)/(np.linalg.norm(actual))))


# Score/accuracy functions


def pure_accuracy(predicted, actual, tolerance=2 * np.finfo('float64').eps):
    return np.mean(np.absolute(predicted - actual) <= tolerance)


def inv_norm_err(predicted, actual):
    return 1.0/norm_err(predicted, actual)


def complement_err_acc(predicted, actual, error=rms_error):
    return 1 - error(predicted, actual)


def simple_gauss_acc(predicted, actual, error=mean_abs_error):
    return simple_gaussian(error(predicted, actual))


DEFAULT_SCORE_FUNCTION = simple_gauss_acc
DEFAULT_ERROR_FUNCTION = rms_error
DEFAULT_TRACK_FUNCTION = mean_abs_error


def score_prediction(x, y_predicted, y_actual, score_function=DEFAULT_SCORE_FUNCTION, rounding=False):
    if y_predicted.shape != y_actual.shape:
        raise RuntimeError('Shape mismatch, predicted had shape {predicted_shape} while actual had shape {actual_shape}'
                           .format(predicted_shape=y_predicted.shape, actual_shape=y_actual.shape))
    return score_function((np.round(y_predicted) if rounding else y_predicted), y_actual)


# # TODO: Change to eval batch predictions and refactor score_ml_model
# def eval_predictions(x_data, y_predicted_data, y_actual_data):  # Potentially useful for series data
#     pass


def score_ml_model(model, x_data, y_data,
                   batch_size=EVAL_BATCH_SIZE, n_epochs=N_EPOCHS, n_pre_training=N_PRE_TRAINING,
                   score_function=DEFAULT_SCORE_FUNCTION, train_after_testing=True):

    n_x = x_data.shape[0]  # Number of x entries
    n_y = y_data.shape[0]  # Number of y entries
    if n_x != n_y:
        _log.warning('x and y data do not have the same number of entries')

    max_i = min(n_x, n_y)
    n_batches = int(ceil(max_i / batch_size))
    scores = np.zeros((n_epochs, n_batches))

    # Train one batch for shape
    _log.log(level=TRAIN_LOG_LEVEL, msg='Pre-training')
    for i in range(0, n_pre_training):
        _log.log(level=TRAIN_ELEMENT_LOG_LEVEL, msg=str(i + 1) + '/' + str(n_pre_training))
        x = x_data[i]
        y = y_data[i]
        model.learn(x, y)

    for epoch_i in range(n_epochs):
        _log.log(level=EPOCH_LOG_LEVEL, msg='Epoch ' + str(epoch_i + 1) + '/' + str(n_epochs))
        data_i = n_pre_training if epoch_i == 0 else 0
        # Go through each batch, test, then train
        for batch_i in range(n_batches):
            batch_max_i = min(data_i + batch_size, max_i)
            _log.log(level=BATCH_LOG_LEVEL, msg='Batch ' + str(batch_i + 1) + '/' + str(n_batches))
            _log.log(level=BATCH_LOG_LEVEL, msg='Index range: ' + str([data_i, batch_max_i]))
            # Test
            _log.log(level=TEST_LOG_LEVEL, msg='Testing')
            batch_scores = np.zeros((batch_max_i-data_i,))
            for i in range(data_i, batch_max_i):
                x = x_data[i]
                y = y_data[i]
                prediction = model.predict(x)
                score = score_prediction(x, prediction, y, score_function=score_function)
                batch_scores[i-data_i] = score
                _log.log(level=TEST_ELEMENT_LOG_LEVEL, msg='x:' + str(x))
                _log.log(level=TEST_ELEMENT_LOG_LEVEL, msg='y:' + str(y))
                _log.log(level=TEST_ELEMENT_LOG_LEVEL, msg='Prediction: ' + str(prediction))
                _log.log(level=TEST_ELEMENT_LOG_LEVEL, msg='Score: ' + str(score))
            batch_score = np.mean(batch_scores)
            scores[epoch_i][batch_i] = batch_score
            _log.log(level=TEST_LOG_LEVEL, msg='Average score:' + str(batch_score))
            if train_after_testing:
                # Train
                _log.log(level=TRAIN_LOG_LEVEL, msg='Training')
                for i in range(data_i, batch_max_i):
                    x = x_data[i]
                    y = y_data[i]
                    model.learn(x, y)
                    _log.log(level=TRAIN_ELEMENT_LOG_LEVEL, msg='Trained on data at ' + str(i))
            data_i = data_i + batch_size
    return scores


def score_ml_models(models, x_data, y_data, score_function=DEFAULT_SCORE_FUNCTION):
    performance = {}
    _log.info('Scoring models')
    for mdl in models:
        _log.info('\tScoring model: ' + str(mdl))
        performance[mdl] = score_ml_model(mdl, x_data, y_data, score_function=score_function)
    scores = {mdl: np.mean(performance[mdl]) for mdl in performance.keys()}
    _log.info('Scoring complete, model performances:')
    for s in scores.items():
        _log.info('\t' + str(s))
    return scores

# For AI models

# TODO
