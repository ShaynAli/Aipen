from flask import Flask, request, jsonify, render_template
from bokeh.embed import components
import data_utils.visualization as vs
import os
from uuid import uuid4
from activities.stock_prediction.stock_prediction import *
from activities.stock_prediction.stock_prediction_models import *
from arena.arena import MachineLearningArena
from collections import defaultdict
from itertools import count, chain
from inspect import getsource


# region Activity configuration

activity_names = {
    FrankfurtStockPrediction: 'Frankfurt Stock Prediction'
}

activity_descriptions = {
    FrankfurtStockPrediction: "Use the opening price of a few stocks from the Frankfurt Exchange to anticipate the "
                              "price of a few other stocks.\n"
}

activities_to_models = {
    FrankfurtStockPrediction: [RandomRangePredictor, MeanPredictor, MeanRowPredictor, ShallowNeuralNetworkPredictor,
                               RandomDepthNeuralNetworkPredictor]
}

model_names = {
    RandomRangePredictor: 'Random Range Model',
    MeanPredictor: 'Mean Model',
    MeanRowPredictor: 'Mean Row Model',
    ShallowNeuralNetworkPredictor: 'Shallow Neural Network',
    RandomDepthNeuralNetworkPredictor: 'Random Depth Neural Network'
}

# endregion

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
    'plot_script': plot_script,
    'plot_view': plot_view,
    'frontend_script': frontend_script
}


def new_uuid():
    return str(uuid4())


# Static dicts
id_to_activity = {new_uuid(): activity for activity in activities_to_models}
activity_to_id = {activity: activity_id for activity_id, activity in id_to_activity.items()}

id_to_model = {new_uuid(): model for model_list in activities_to_models.values() for model in model_list}
model_to_id = {model: model_id for model_id, model in id_to_model.items()}
model_to_source = {model: getsource(model) for model in chain(*activities_to_models.values())}

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

    arena = MachineLearningArena(model_pool=models, activity=activity, generation_size=20)

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
def arena_generation_scores(arena_id, generation_number):
    try:
        generation_number = int(generation_number)
        arena = id_to_arena[arena_id]
        model_scores = arena.score_history[generation_number]
        model_id_to_score = {model_instance_id[model]: score for model, score in model_scores.items()}
        model_to_names = {model: model_names[type(model)] for model in model_scores}
        leaderboard = []
        for model, model_name in model_to_names.items():
            model_id = model_instance_id[model]
            model_score = model_id_to_score[model_id]
            leaderboard.append((model_name, model_id, model_score))
        leaderboard.sort(key=lambda e: e[2], reverse=True)
    except (ValueError, IndexError):
        print(f'Invalid generation number {generation_number} for arena {arena_id}')
        return jsonify(success=False)
    print(f'Returning generation {generation_number} results for arena {arena_id}')
    return jsonify(success=True, leaderboard=leaderboard)


@app.route('/arena/<arena_id>/generation_plot/<start>/<end>', methods=http_methods)
def arena_generation_plot_update(arena_id, start, end):
    try:
        arena = id_to_arena[arena_id]
    except KeyError:
        print(f'Unable to find arena {arena_id}')
        return jsonify(success=False)
    if start == 'start' or start == 'START':
        start = 0
    if end == 'end' or end == 'END':
        end = len(arena.score_history)
    plot_dict = defaultdict(list)
    for generation_no, generation in zip(count(start), arena.score_history[start:end]):
        for model, score in generation.items():
            model_id = model_instance_id[model]
            plot_dict[f'{model.__class__.__name__}-{model_id[:8]}'].append((generation_no, score))

    if not plot_dict.keys():
        return render_template('plot.html', **elements)

    new_plot = vs.multi_line(plot_dict, "Generation", "Score")

    new_script, new_view = components(new_plot)

    elements['plot_script'] = new_script
    elements['plot_view'] = new_view

    return render_template('plot.html', **elements)


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
    model = id_to_model[model_id]
    model_name = model_names[model]
    model_source = model_to_source[model]
    return jsonify(success=True, name=model_name, preview=model_source, secondary_preview=model.description())

# endregion


# region Activities routes

@app.route('/activity', methods=http_methods)
def get_activities():
    print(f'Returning all activities')
    return jsonify(success=True, activity_ids=[activity_id for activity_id in id_to_activity],
                   activity_names=[activity_names[activity] for activity in activity_to_id])


@app.route('/activity/<activity_id>', methods=http_methods)
def get_activity(activity_id):
    try:
        activity = id_to_activity[activity_id]
        print(f'Returning activity {activity_id}')
        return jsonify(success=True, name=activity_names[activity],
                       preview=activity_descriptions[activity], secondary_preview='')
    except KeyError:
        print(f'Could not find activity {activity_id}')
        return jsonify(success=False)


@app.route('/activity/<activity_id>/models', methods=http_methods)
def get_models(activity_id):
    print(f'Returning models for activity {activity_id}')
    activity = id_to_activity[activity_id]
    models = activities_to_models[activity]
    return jsonify(succes=True, model_ids=[model_to_id[model] for model in models],
                   model_names=[model_names[model] for model in models])

# endregion


if __name__ == "__main__":
    app.run(debug=debug)
