from flask import Flask
import os
import pdb

app = Flask(__name__)

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

debug = True

with open(os.path.join(__location__, 'assets', 'style.css')) as style_file:
    style = style_file.read()


elements = {
    'style': style

}


@app.route('/')
def home():
    try:
        with open(os.path.join(__location__, 'templates', 'index.html')) as template_page:
            return template_page.read().format(**elements)
    except Exception as e:
        if not debug:
            raise e
        print(f'Encountered exception {type(e)} {e}')
        pdb.set_trace()


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
