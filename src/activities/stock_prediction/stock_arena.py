from arena.arena import MachineLearningArena
from activities.stock_prediction.stock_prediction import FrankfurtStockPrediction
from activities.stock_prediction.stock_prediction_models import RandomRangePredictor
import pprint

if __name__ == '__main__':

    arena = MachineLearningArena(model_pool=[RandomRangePredictor], activity=FrankfurtStockPrediction)
    printer = pprint.PrettyPrinter()
    for _ in range(10):
        arena.auto_compete()
        printer.pprint(arena.score_history[-1])
