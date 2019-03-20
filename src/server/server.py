from flask import Flask, request, jsonify, render_template
from bokeh.embed import components
import data_utils.data as dt
import data_utils.visualization as vs
import os

app = Flask(__name__)

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

debug = True

with open(os.path.join(__location__, 'assets', 'style.css')) as style_file:
    style = style_file.read()

with open(os.path.join(__location__, 'assets' '/script.js')) as functionality_script:
    frontend = functionality_script.read()

# Test plot to see how it displays
data = {
    "model1": [(0, 1), (1, 2), (2, 4)],
    "model2": [(0, 4), (1, 5), (2, 6)],
    "model3": [(0, 10), (1, 15), (2, 20), (3, 20)]
}

test_plot = vs.empty_plot()

# Separate the functionality and the view
plot_script, plot_view = components(test_plot)

elements = {
    'style': style,
    'plot_script': plot_view,
    'plot_view': plot_script,
    'frontend': frontend
}


@app.route('/')
def home():
        return render_template('index.html', **elements)


@app.route('/start_arena', methods=['POST'])
def start_arena():
    print(request.json)
    return jsonify(request.json)


@app.route('/request', methods=['POST'])
def fulfill_request():
    print(request.json)
    return jsonify(request.json)


@app.route('/update_plot', methods=['POST'])
def update_plot():
    test_data = dt.Data(data=dt.indexed_linear_noise_data(50, 100))
    test_plot_update = vs.plot_line(test_data, "Generation", "Accuracy")

    # Separate the functionality and the view
    plot_script_update, plot_view_update = components(test_plot_update)

    elements['plotScript'] = plot_script_update
    elements['plotView'] = plot_view_update

    return render_template('plot.html', **elements)


@app.route('/assets/<asset_name>')
def asset(asset_name):
    try:
        with open(os.path.join(__location__, 'assets', asset_name)) as asset:
            return asset.read()
    except FileNotFoundError:
        print(f'Unable to locate asset {asset_name}')
        return f'Unable to locate asset {asset_name}'


if __name__ == "__main__":
    app.run(debug=debug)
