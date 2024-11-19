from flask import Flask
from flask_restx import Api
from app.api.v1.users import api as users_ns
from app.api.v1.amenities import api as amenities_ns
from app.api.v1.places import api as places_ns
from app.api.v1.reviews import api as reviews_ns
# from flask_bcrypt import Bcrypt
# from flask_jwt_extended import JWTManager

# bcrypt = Bcrypt()
# jwt = JWTManager()

def create_app(config_class='config.DevelopmentConfig'):
    app = Flask(__name__)
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API')
    app.config.from_object(config_class)  # Load the configuration from the specified class
    # bcrypt.init_app(app)
    # jwt.init_app(app)

    # Register the users namespace
    api.add_namespace(users_ns, path='/api/v1/users')
    # Register the amenities namespace
    api.add_namespace(amenities_ns, path='/api/v1/amenities')
    # Register the places namespace
    api.add_namespace(places_ns, path='/api/v1/places')
    # Register the reviews namespace
    api.add_namespace(reviews_ns, path='/api/v1/reviews')
    return app
