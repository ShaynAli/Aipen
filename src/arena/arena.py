import evaluation
from random import choice
from pandas import isnull

class MachineLearningArena:

    def __init__(self, model_pool, activity, score_function=evaluation.DEFAULT_SCORE_FUNCTION, generation_size=10):
        self.model_pool = model_pool
        self.activity = activity()
        self.score_function = score_function
        self.models = list(self.new_models(n_models=generation_size))
        self.score_history = []

    def new_model(self):
        return choice(self.model_pool)(self.activity)

    def new_models(self, n_models):
        return (self.new_model() for _ in range(n_models))

    def compete(self, x, y, live_ratio=0.5):
        model_score = {m: evaluation.score(m, x, y, score_function=self.score_function) for m in self.models}
        self.score_history.append(model_score)
        score_ranking = sorted(model_score.keys(), key=lambda model: model_score[model], reverse=True)
        from utilities import partition_indices
        start_i, keep_i, kill_i = partition_indices(score_ranking, live_ratio)
        self.models[keep_i:kill_i] = self.new_models(kill_i - keep_i)

    def auto_compete(self, live_ratio=0.5):
        x, y = self.activity.next_data()
        while isnull(x).any() or isnull(y).any():
            x, y = self.activity.next_data()
        self.compete(x=x, y=y, live_ratio=live_ratio)
