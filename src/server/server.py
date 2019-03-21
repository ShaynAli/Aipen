from flask import Flask, request, jsonify, render_template
from bokeh.embed import components
import data_utils.data as dt
import data_utils.visualization as vs
import os

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

# region Homepage


@app.route('/')
def home():
        return render_template('index.html', **elements)

# endregion

# region Arena routes


@app.route('/arena/new_arena')
def new_arena():
    pass


@app.route('/arena/<arena_id>')
def arena(arena_id):
    pass


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
