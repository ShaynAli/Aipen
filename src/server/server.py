from flask import Flask, request, jsonify, render_template
from bokeh.embed import components
import data_utils.visualization as vs
import os
from uuid import uuid4
from activities.stock_prediction.stock_prediction import FrankfurtStockPrediction
from activities.stock_prediction.stock_prediction_models import RandomRangePredictor
from arena.arena import MachineLearningArena
from collections import defaultdict
import pdb

app = Flask(__name__)
http_methods = ['POST', 'GET']

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

debug = True


def asset(asset_name):
    with open(os.path.join(__location__, 'assets', asset_name)) as asset_file:
        return asset_file.read()


style = asset('style.css')
frontend_script = asset('script.js')

test_plot = vs.empty_plot()
plot_script, plot_view = components(test_plot)

elements = {
    'style': style,
    'plot_script': plot_view,
    'plot_view': plot_script,
    'frontend_script': frontend_script
}

# Configuration dicts
activity_names = {
    FrankfurtStockPrediction: 'Frankfurt Stock Prediction'
}

model_names = {
    RandomRangePredictor: 'Random Range Predictor'
}

activities_to_models = {
    FrankfurtStockPrediction: [RandomRangePredictor]
}


def new_uuid():
    return str(uuid4())


# Static dicts
id_to_activity = {new_uuid(): activity for activity in activities_to_models}
activity_to_id = {activity: activity_id for activity_id, activity in id_to_activity.items()}

id_to_model = {new_uuid(): model for model_list in activities_to_models.values() for model in model_list}
model_to_id = {model: model_id for model_id, model in id_to_model.items()}

# Dynamic dicts
id_to_arena = {}
arena_to_id = {}
arena_id_started = {}
model_instance_id = defaultdict(new_uuid)


# region Homepage


@app.route('/', methods=http_methods)
def home():
        return render_template('index.html', **elements)

# endregion

# region Arena routes


@app.route('/arena', methods=http_methods)
def get_arenas():
    return jsonify(success=True, arena_ids=[arena_id for arena_id in id_to_arena])


@app.route('/arena/new_arena', methods=http_methods)
def new_arena():

    model_ids = request.json['models']
    models = [id_to_model[model_id] for model_id in model_ids]
    activity_id = request.json['activity']
    activity = id_to_activity[activity_id]

    arena = MachineLearningArena(model_pool=models, activity=activity)

    arena_id = new_uuid()
    id_to_arena[arena_id] = arena
    arena_to_id[arena] = arena_id
    arena_id_started[arena_id] = False

    return jsonify(success=True, arena_id=arena_id)


@app.route('/arena/<arena_id>', methods=http_methods)
def get_arena(arena_id):
    print(f'Returning arena {arena_id}')
    if arena_id in id_to_arena:
        return jsonify(success=True)
    return jsonify(success=False)


@app.route('/arena/<arena_id>/start', methods=http_methods)
def start_arena(arena_id):
    arena_id_started[arena_id] = True
    arena = id_to_arena[arena_id]
    print(f'Staring arena {arena_id}')
    while arena_id_started[arena_id]:
        print(f'Running generation {len(arena.score_history) + 1} for arena {arena_id}')
        arena.auto_compete()
    return jsonify(success=True)


@app.route('/arena/<arena_id>/stop', methods=http_methods)
def stop_arena(arena_id):
    try:
        arena_id_started[arena_id] = False
    except KeyError:
        print(f'Could not stop arena {arena_id} since this id is unrecognized')
        return jsonify(success=False)
    print(f'Stopping arena {arena_id}')
    return jsonify(success=True)


@app.route('/arena/<arena_id>/generation/<generation_number>', methods=http_methods)
def arena_generation_score(arena_id, generation_number):
    try:
        generation_number = int(generation_number)
        arena = id_to_arena[arena_id]
        model_scores = arena.score_history[generation_number]
        model_id_to_score = {model_instance_id[model]: score for model, score in model_scores.items()}
    except (ValueError, IndexError):
        print(f'Invalid generation number {generation_number} for arena {arena_id}')
        return jsonify(success=False)
    print(f'Returning generation {generation_number} results for arena {arena_id}')
    return jsonify(success=True, scores=model_id_to_score)


@app.route('/arena/<arena_id>/set_models', methods=http_methods)
def set_models(arena_id):
    arena = id_to_arena[arena_id]
    new_model_pool = [id_to_model[model_id] for model_id in request.json]
    if not new_model_pool:
        print(f'Refused to set model pool of {arena_id} to empty')
        return jsonify(success=False)
    arena.model_pool = new_model_pool
    print(f'Set model pool of {arena_id} to {new_model_pool}')
    return jsonify(success=True)


# endregion

# region Model routes


@app.route('/model/<model_id>', methods=http_methods)
def get_model(model_id):
    print(f'Returning model {model_id}')
    return jsonify(success=True, model_name=id_to_model[model_id])

# endregion


# region Activities routes

@app.route('/activity', methods=http_methods)
def get_activities():
    print(f'Returning all activities')
    return jsonify(activity_ids=[activity_id for activity_id in id_to_activity],
                   activity_names=[activity_names[activity] for activity in activity_to_id])


@app.route('/activity/<activity_id>/models', methods=http_methods)
def get_models(activity_id):
    print(f'Returning models for activity {activity_id}')
    activity = id_to_activity[activity_id]
    models = activities_to_models[activity]
    return jsonify(model_ids=[model_to_id[model] for model in models],
                   model_names=[model_names[model] for model in models])

# endregion


if __name__ == "__main__":
    app.run(debug=debug)
