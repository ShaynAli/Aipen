from flask import Flask, request, jsonify, render_template
from bokeh.embed import components
import data_utils.data as dt
import data_utils.visualization as vs
import arena.arena as arena
import os
from uuid import uuid4
from activities.stock_prediction.stock_prediction import FrankfurtStockPrediction
from activities.stock_prediction.stock_prediction_models import RandomRangePredictor
from arena.arena import MachineLearningArena

app = Flask(__name__)

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

debug = True


def asset(asset_name):
    with open(os.path.join(__location__, 'assets', asset_name)) as asset_file:
        return asset_file.read()


style = asset('style.css')
frontend = asset('script.js')

test_plot = vs.empty_plot()
plot_script, plot_view = components(test_plot)

elements = {
    'style': style,
    'plot_script': plot_view,
    'plot_view': plot_script,
    'frontend': frontend
}

id_to_activity = {uuid4(): activity for activity in [FrankfurtStockPrediction]}
activity_to_id = {activity: activity_id for activity_id, activity in id_to_activity.items()}

id_to_model = {uuid4(): model for model in [RandomRangePredictor]}
model_to_id = {model: model_id for model_id, model in id_to_model.items()}

id_to_arena = {}
arena_to_id = {}

# region Homepage


@app.route('/')
def home():
        return render_template('index.html', **elements)

# endregion

# region Arena routes


@app.route('/arena')
def get_arenas():
    return jsonify([arena_id for arena_id in id_to_arena])
    # Return all ids of arenas (and optionally their names)
#     ids: [ 942039, 2348923 ]


@app.route('/arena/new_arena')
def new_arena():

    requests = {
        'activity': "activity_id",
        'models': ["IDs"]
    }

    n_arena = arena.MachineLearningArena(model_pool=requests['models'], activity=requests['activity'])
    arena_id = uuid4()
    id_to_arena[arena_id] = n_arena
    arena_to_id[n_arena] = arena_id

    return jsonify(arena_id=arena_id)


@app.route('/arena/<arena_id>')
def arena(arena_id):
    pass
    # Return name of arena + other info


@app.route('/arena/<arena_id>/start')
def start_arena(arena_id):
    pass


@app.route('/arena/<arena_id>/stop')
def stop_arena(arena_id):
    pass


@app.route('/arena/<arena_id>/generation/<generation_number>')
def arena_generation_score(arena_id, generation_number):
    pass


@app.route('/arena/<arena_id>/set_models')
def set_models(arena_id):
    pass


# endregion

# region Model routes


@app.route('/model/<model_id>')
def model(model_id):
    pass

# endregion


if __name__ == "__main__":
    app.run(debug=debug)
