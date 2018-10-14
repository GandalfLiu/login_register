from flask_bootstrap import Bootstrap
from flask_caching import Cache
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
cache = Cache(config={'CACHE_TYPE':'redis','CACHE_KEY_PREFIX':'python(Flask)'})


def init_ext(app):
    db.init_app(app)
    migrate.init_app(app,db)
    Bootstrap(app)
    # DebugToolbarExtension(app)
    cache.init_app(app)






