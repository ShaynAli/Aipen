""" arena.py - Where ML and AI bots go to face off """
import evaluation


class MachineLearningArena:

    def __init__(self, model_pool, activity, generation_size=10):
        self.model_pool = model_pool
        self.activity = activity
        self.models = self.new_models(n_models=generation_size)
        self.score_history = []

    def new_model(self):
        from random import choice
        return choice(self.model_pool)(x_shape=self.activity.x_shape, y_shape=self.activity.y_shape)

    def new_models(self, n_models):
        return (self.new_model() for _ in range(n_models))

    def compete(self, x, y, live_ratio=0.5, score_function=evaluation.DEFAULT_SCORE_FUNCTION):
        model_score = {m: evaluation.score(m, x, y, score_function=score_function) for m in self.models}
        self.score_history.append(model_score)
        score_ranking = sorted(model_score.keys(), key=lambda model: model_score[model], reverse=True)
        from utilities import partition_indices
        start_i, keep_i, kill_i = partition_indices(score_ranking, live_ratio)
        self.models[keep_i:kill_i] = self.new_models(kill_i - keep_i)

    def auto_compete(self, live_ratio=0.5):
        x, y = self.activity.next_data()
        self.compete(x=x, y=y, live_ratio=live_ratio, score_function=evaluation.DEFAULT_SCORE_FUNCTION)
