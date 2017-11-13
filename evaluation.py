''' evaluation.py - Evaluates AI and ML models '''
from log import logger
from math import ceil
import numpy as np

# TODO Break apart ML and AI files into different modules

logging = logger.get('evaluation')

# For ML models
EVAL_BATCH_SIZE = 5
N_EPOCHS = 1
N_PRE_TRAINING = 1


def accuracy(predicted, actual, rounding=False):
    if predicted.shape != actual.shape:
        raise RuntimeError('Shape mismatch, predicted had shape {predicted_shape} while actual had shape {actual_shape}'
                           .format(predicted_shape=predicted.shape, actual_shape=actual.shape))
    err = np.round(predicted) - actual if rounding else predicted - actual
    abs_err = np.absolute(err)
    return 1 - np.mean(abs_err)


def score_prediction(x, y_predicted, y_actual, score=accuracy):
    return score(y_predicted, y_actual)

# # TODO: Change to eval batch predictions and refactor score_ml_model
# def eval_predictions(x_data, y_predicted_data, y_actual_data):  # Potentially useful for series data
#     pass


def score_ml_model(model, x_data, y_data, batch_size=EVAL_BATCH_SIZE, n_epochs=N_EPOCHS, n_pre_training=N_PRE_TRAINING):
    # TODO
    '''
    
    First entries will be trained but not tested on, this allows the model to learn the shape of the input and output
    :param model: 
    :param x_data: 
    :param y_data: 
    :param batch_size: 
    :param n_epochs: 
    :param n_pre_training: Number of entries to pre-train on
    :return: 
    '''

    n_x = x_data.shape[0]  # Number of x entries
    n_y = y_data.shape[0]  # Number of y entries
    if n_x != n_y:
        logging.warning('x and y data do not have the same number of entries')

    max_i = min(n_x, n_y)
    n_batches = int(ceil(max_i / batch_size))
    scores = np.zeros((n_epochs, n_batches))

    # Train one batch for shape
    logging.info('\tPre-training')
    for i in range(0, n_pre_training):
        logging.info('\t\t' + str(i + 1) + '/' + str(n_pre_training))
        x = x_data[i]
        y = y_data[i]
        model.learn(x, y)

    for epoch_i in range(n_epochs):
        logging.info('\tEpoch ' + str(epoch_i + 1) + '/' + str(n_epochs))
        data_i = n_pre_training if epoch_i == 0 else 0
        # Go through each batch, test, then train
        for batch_i in range(n_batches):
            batch_max_i = min(data_i + batch_size, max_i)
            logging.info('\t\tBatch ' + str(batch_i + 1) + '/' + str(n_batches))
            logging.info('\t\tIndex range: ' + str([data_i, batch_max_i]))
            # Test
            logging.info('\t\t\tTesting')
            batch_scores = np.zeros((batch_max_i-data_i,))
            for i in range(data_i, batch_max_i):
                x = x_data[i]
                y = y_data[i]
                batch_scores[i-data_i] = score_prediction(x, model.predict(x), y)
            batch_score = np.mean(batch_scores)
            scores[epoch_i][batch_i] = batch_score
            logging.info('\t\t\tAverage score:' + str(batch_score))
            # Train
            logging.info('\t\t\tTraining')
            for i in range(data_i, batch_max_i):
                x = x_data[i]
                y = y_data[i]
                model.learn(x, y)
            data_i = data_i + batch_size
    return scores


def score_ml_models(models, x_data, y_data):
    performance = {}
    logging.info('Scoring models')
    for mdl in models:
        logging.info('Model: ' + str(mdl))
        performance[mdl] = score_ml_model(mdl, x_data, y_data)
    scores = {mdl: np.mean(performance[mdl]) for mdl in performance.keys()}
    logging.info('Scoring complete, model performances:')
    for s in scores:
        logging.info('\t' + str(s))
    return scores


# For AI models

# TODO
