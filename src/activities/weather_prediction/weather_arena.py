from arena.arena import MachineLearningArena
from activities.weather_prediction.weather_prediction import HungaryWeatherPrediction
from activities.weather_prediction.weather_prediction_models import RandomRangePredictor
import pprint

if __name__ == '__main__':

    arena = MachineLearningArena(model_pool=[RandomRangePredictor], activity=HungaryWeatherPrediction)
    printer = pprint.PrettyPrinter()
    for _ in range(10):
        arena.auto_compete()
        printer.pprint(arena.score_history[-1])
