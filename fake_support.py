from flask import Flask

test = Flask(__name__)


@test.route("/")
def index():
    return "Hello !!!!"


test.run()
