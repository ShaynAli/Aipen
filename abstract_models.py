''' super_model.py - An abstract ML model for all other Aipen models to inherit from '''

from abc import ABCMeta, abstractmethod


class MLModel(metaclass=ABCMeta):
    '''
    Abstract class for all ML_Models to implement
    Expected methods to implement:
        __init__()
        learn(x, y)
        predict(x)
    Optional implementation:
        summary()
        name()
    '''

    @abstractmethod
    def __init__(self):
        '''
        Initialize the model
        '''

    @abstractmethod
    def predict(self, x):
        '''
        Predict labels corresponding to the predictors
        :param x: Inputs to the model (x values) in a pandas DataFrame
        :return: Estimated labels (y values) in a pandas DataFrame
        '''

    @abstractmethod
    def learn(self, x, y):
        '''
        Fit/train/learn the corresponding predictors and labels
        :param x: Inputs to the model (x values) in a pandas DataFrame
        :param y: True outputs corresponding to the predictors (y values) in a pandas DataFrame
        '''

    def summary(self):
        '''
        A summary of the model
        Does not need to be implemented
        :return: A string which summarizes the model and parameters
        '''
        return '''
            Model\n
            \tAbstract superclass for all Models to implement
            '''

    def name(self):
        '''
        Returns the name of the model, should fit on one line
        By default, returns the class name, e.g. MutatingMLModel
        Generally should not be overriden
        :return: The name of the model as a short string
        '''
        return self.__class__.__name__


class EvolutionaryMLModel(MLModel):

    mutations = {}  # Dict of possible mutations

    @abstractmethod
    def mutate(self):
        '''
        Change model hyper-parameters to potentially produce a better model
        The model should draw from the dict of possible mutations, mutations
        '''

    def simplify(self, preserving=True):
        '''
        Simplify model to reduce computation complexity
        Preserving simplifications reduce computational complexity without changing the output, however they may affect
        how the system mutates in the future
        Non-preserving simplifications reduce computational complexity, but may affect the output, they should aim to 
        eliminate low-weight, high-computation parts of the system
        :param preserving: Whether the model is exactly preserved or not
        '''

    def __init__(self):
        super(EvolutionaryMLModel, self).__init__()

    def predict(self, x):
        super(EvolutionaryMLModel, self).predict()

    def learn(self, x, y):
        super(EvolutionaryMLModel, self).learn()

    def summary(self):
        return ('''
            MutatingMLModel\n
            \tAbstract class for mutating ML models to implement so they can be used in evolutionary search
            ''')


class AIModel(metaclass=ABCMeta):
    # TODO
    pass
