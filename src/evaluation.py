""" evaluation.py - Evaluates AI and ML models """
from math import ceil, isnan
import numpy as np

# For ML models
EVAL_BATCH_SIZE = 5
N_EPOCHS = 1
N_PRE_TRAINING = 1

# region Mathematical functions


def gaussian(x, a=1, mu=0, sigma=1):
    return a*np.exp(-(((x - mu)/(2.*sigma))**2))


def simple_gaussian(x):
    return np.exp(-(x**2))

# endregion


# region Error functions

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

# endregion


# region Accuracy functions

def tolerant_binary_accuracy(predicted, actual, tolerance=0.001):
    return np.mean(np.absolute(predicted - actual) <= tolerance*actual)


def inv_norm_err(predicted, actual):
    return 1.0/norm_err(predicted, actual)


def complement_err_acc(predicted, actual, error=rms_error):
    return 1 - error(predicted, actual)


def simple_gauss_acc(predicted, actual, error=mean_abs_error):
    return simple_gaussian(error(predicted, actual))


def complement_mean_pct_error(predicted, actual):
    return 1 - mean_pct_error(predicted, actual)

# endregion


# region Model scoring

DEFAULT_SCORE_FUNCTION = inv_norm_err
DEFAULT_ERROR_FUNCTION = rms_error
DEFAULT_TRACK_FUNCTION = rms_error


def score(model, x, y, score_function=DEFAULT_SCORE_FUNCTION, train_after_testing=True):
    try:
        model_score = score_function(model.predict(x), y)
        if isnan(model_score):
            model_score = 0
    except BaseException as e:
        print(f'Model {model.__class__.__name__} encountered exception {e.__class__.__name__} {e} during scoring')
        model_score = 0
    try:
        if train_after_testing:
            model.train(x, y)
    except BaseException as e:
        pass
        print(f'Model {model.__class__.__name__} encountered exception {e.__class__.__name__} {e} during training')
    return model_score

# endregion
