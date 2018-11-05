""" super_model.py - An abstract ML model for all other Aipen models to inherit from """
from abc import ABCMeta, abstractmethod
import pickle


class Model:

    # region Serialization

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

    # endregion

    # region Equality

    def __hash__(self):
        """
        This causes models with the exact same parameters (and object data in general) to have the same hash
        """
        return hash(str(sorted(self.__dict__.items())))

    def __eq__(self, other):
        """
        Compares model's hashes, which will be equal if their parameters are equal
        """
        # TODO: Fix - for RandomStaticModels this check fails
        return hash(self) == hash(other)

    # endregion


class MLModel(Model, metaclass=ABCMeta):
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
        Initialize the model
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


class EvolutionaryModel(Model, metaclass=ABCMeta):  # TODO: Make more rigorous

    @abstractmethod
    def __init__(self):
        """
        Initialize the model
        """

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


class AgentModel(Model, metaclass=ABCMeta):  # TODO
    pass
