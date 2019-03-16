from flask import Flask
import os
import pdb

app = Flask(__name__)

html_elements = {
    'test': 'test out'
}

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

debug = False


@app.route('/', methods=['GET'])
def home_page():
    try:
        return render_home_page()
    except Exception as e:
        print(f'Encountered exception {type(e)} {e}')
        return f'Failed with exception {type(e)} {e}'


def render_home_page():
    try:
        with open(os.path.join(__location__, 'index.html')) as template_page:
            template_string = template_page.read()
        return template_string.format(**html_elements)
    except Exception as e:
        if not debug:
            raise e
        print(f'Encountered exception {type(e)} {e}')
        pdb.set_trace()


if __name__ == "__main__":
    app.run(debug=True)
