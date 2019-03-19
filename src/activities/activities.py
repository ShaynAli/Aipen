from abc import ABCMeta, abstractmethod

# region AI


class InvalidAction(Exception):
    pass


class Activity(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def n_players():
        pass

    def __init__(self):
        pass

    @abstractmethod
    def state(self, agent):
        pass

    @abstractmethod
    def score(self, agent):
        pass

    class Action(metaclass=ABCMeta):
        pass

    @abstractmethod
    def actions(self, agent):
        pass

    @abstractmethod
    def act(self, agent, *actions):
        valid_actions = actions(agent)
        if not all(action in valid_actions for action in actions):
            raise InvalidAction(f'Some of the following actions are invalid: {actions}')
        pass

    class Agent(metaclass=ABCMeta):

        def __init__(self, activity):
            self.activity = activity

        @abstractmethod
        def act(self):
            pass


class RandomAgent(Activity.Agent):

    def __init__(self, activity: Activity):
        super().__init__(activity)

    def act(self):
        from random import choice
        self.activity.act(self, choice(self.activity.actions(self)))


# endregion

# region ML


class MachineLearningActivity(metaclass=ABCMeta):

    @abstractmethod
    @property
    def x_shape(self):
        pass

    @abstractmethod
    @property
    def y_shape(self):
        pass

    class Model(metaclass=ABCMeta):

        def __init__(self):
            pass

        @abstractmethod
        def learn(self, x, y):
            pass

        @abstractmethod
        def predict(self, x):
            pass


# endregion
