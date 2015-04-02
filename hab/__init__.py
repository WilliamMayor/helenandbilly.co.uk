import os

from flask import Flask

import assets
import blueprint


def boolify(s):
    if s == 'True':
        return True
    if s == 'False':
        return False
    raise ValueError("%s is not one of 'True' or 'False'" % s)


def auto_convert(s):
    for fn in (boolify, int, float):
        try:
            return fn(s)
        except ValueError:
            pass
    return s


def create_app():
    app = Flask(__name__)

    app.config.from_object('hab.config')
    app.config.update({
        k: auto_convert(os.environ[k])
        for k in app.config
        if k in os.environ})

    assets.init_app(app)

    app.register_blueprint(blueprint.bp)
    return app
