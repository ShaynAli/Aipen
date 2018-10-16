""" super_model.py - An abstract ML model for all other Aipen models to inherit from """
from abc import ABCMeta, abstractmethod
import pickle


class MLModel(metaclass=ABCMeta):
    """
    Abstract class for all ML_Models to implement
    Expected fields or properties for access
    Expected methods to implement:
        __init__()
        learn(x, y)
        predict(x)
    Optional implementation:
        summary()
        name()
    """

    @abstractmethod
    def __init__(self):
        """
        Initialize the model with random properties and mutations
        """

    @abstractmethod
    def predict(self, x):
        """
        Predict labels corresponding to the predictors
        :param x: Inputs to the model (x values) in a pandas DataFrame
        :return: Estimated labels (y values) in a pandas DataFrame
        """

    @abstractmethod
    def learn(self, x, y):
        """
        Fit/train/learn the corresponding predictors and labels
        :param x: Inputs to the model (x values) in a pandas DataFrame
        :param y: True outputs corresponding to the predictors (y values) in a pandas DataFrame
        """

    @abstractmethod
    def properties(self):
        """
        A list of properties about the model
        :return: A dict of properties related to the model
        """

    def summary(self):
        """
        A summary of the model
        Does not need to be implemented
        :return: A string which summarizes the model and parameters
        """
        return '''
            Model\n
            \tAbstract superclass for all Models to implement
            '''

    def name(self):
        """
        Returns the name of the model, should fit on one line
        By default, returns the class name, e.g. MutatingMLModel
        Generally should not be overridden
        :return: The name of the model as a short string
        """
        return self.__class__.__name__

    @staticmethod
    def load(load_file):
        f = open(load_file, 'rb')
        mdl = pickle.load(f)
        f.close()
        return mdl

    def save(self, save_file):
        f = open(save_file, 'wb')
        pickle.dump(self, f)
        f.close()


class EvolutionaryMLModel(MLModel):

    @abstractmethod
    def __init__(self):
        super(EvolutionaryMLModel, self).__init__()

    @abstractmethod
    def predict(self, x):
        super(EvolutionaryMLModel, self).predict(x)

    @abstractmethod
    def learn(self, x, y):
        super(EvolutionaryMLModel, self).learn(x, y)

    @abstractmethod
    def mutations(self):
        """
        Ways in which the model can mutate - see .mutate()
        :return: A dict of possible mutations to a generator of possible values
        """

    @abstractmethod
    def properties(self):  # TODO
        pass

    @abstractmethod
    def mutate(self):
        """
        Change model hyper-parameters to potentially produce a better model
        The model should draw from the dict of possible mutations given by .mutations()
        """

    def summary(self):
        return ('''
            MutatingMLModel\n
            \tAbstract class for mutating ML models to implement so they can be used in evolutionary search
            ''')


class AIModel(metaclass=ABCMeta):  # TODO
    pass
