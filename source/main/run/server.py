import logging

from flask import Flask

from source.main.route.price_calculator_route import calculate_price_route

app = Flask(__name__)

log = logging.getLogger('werkzeug')

log.disabled = True
app.register_blueprint(calculate_price_route)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
