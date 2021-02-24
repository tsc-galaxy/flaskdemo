# config=utf-8
from login import userRoute
from model import create_app
from flask import render_template



DEFAULT_MODULES = [userRoute]

app = create_app('../config.py')


for module in DEFAULT_MODULES:
    app.register_blueprint(module)


@app.before_request
def before_request():
    pass


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
