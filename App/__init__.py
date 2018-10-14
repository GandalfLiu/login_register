from flask import Flask

from App.ext import init_ext
from App.settings import config
from App.views import init_views


def createApp(env=None):

    app = Flask(__name__)

    app.config.from_object(config.get(env or 'default'))

    init_views(app)

    init_ext(app)



    return app