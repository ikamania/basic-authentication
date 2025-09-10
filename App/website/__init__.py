from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET KEY'] = 'TOSTERMOSTERMONSTER'
    app.secret_key = 'TOSTERMOSTERMONSTER'
    
    # import 
    from .views import views
    from .auth import auth

    # register
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app