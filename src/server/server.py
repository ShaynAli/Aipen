from flask import Flask, request, jsonify, render_template
from bokeh.embed import components
import data_utils.data as dt
import data_utils.visualization as vs
import os
import pdb

app = Flask(__name__)

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

debug = True

with open(os.path.join(__location__, 'assets', 'style.css')) as style_file:
    style = style_file.read()

with open(os.path.join(__location__, 'assets' '/script.js')) as functionality_script:
    functionScript = functionality_script.read()

# Test plot to see how it displays
testData = dt.Data()
testData.set_linear(50, 2, -50)
testPlot = vs.plot_line(testData, "Generation", "Accuracy")


# Separate the functionality and the view
plotScript, plotView = components(testPlot)

elements = {
    'style': style,
    'plotScript': plotScript,
    'plotView': plotView,
    'functionScript': functionScript
}


@app.route('/')
def home():
    try:
        return render_template('index.html', **elements)

    except Exception as e:
        if not debug:
            raise e
        print(f'Encountered exception {type(e)} {e}')
        pdb.set_trace()


@app.route('/request', methods=['POST'])
def fulfill_request():
    testData.set_linear(100, 2, -50)
    testPlotUpdate = vs.plot_line(testData, "Generation", "Accuracy")

    # Separate the functionality and the view
    plotScriptUpdate, plotViewUpdate = components(testPlotUpdate)

    elements['plotScript'] = plotScriptUpdate
    elements['plotView'] = plotViewUpdate
    update_elements = {
        'plot_script': plotScriptUpdate,
        'plot_view': plotViewUpdate
    }
    return jsonify(update_elements)
    # return jsonify(request.json)


@app.route('/update_plot', methods=['POST'])
def update_plot():
    testData.set_linear(100, 2, -50)
    testPlotUpdate = vs.plot_line(testData, "Generation", "Accuracy")

    # Separate the functionality and the view
    plotScriptUpdate, plotViewUpdate = components(testPlotUpdate)

    elements['plotScript'] = plotScriptUpdate
    elements['plotView'] = plotViewUpdate
    return render_template('plot.html', plotScript=plotScriptUpdate, script_bok=plotViewUpdate)


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
