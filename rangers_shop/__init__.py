from flask import Flask 
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager


# internal imports aka coming from our applications
from config import Config 
from .models import login_manager, db
from .blueprints.site.routes import site  # importing blueprint object
from .blueprints.auth.routes import auth 
from .blueprints.api.routes import api  # remember! - need to register this when getting Insomnia token
from .helpers import JSONEncoder 


# instantiate our Flask app
app = Flask(__name__)  # passing in the name of our directory as the name of our app

# going to tell our app what Class to look to for configuration
app.config.from_object(Config)
jwt = JWTManager(app)  # allows our app to use JWTManager from anywhere


# wrap our whole app in our login_manager so we can use it wherever in our app
login_manager.init_app(app)
login_manager.login_view = 'auth.sign_id'  # authentication route
login_manager.login_message = "Hey you! Login Please"   # use if they go in a route that didnt log in
login_manager.login_message_category = 'warning' # red / green

# creating  our first route using the @route decorator
# @app.route("/")  # "/" endpoint is standard landing/home page endpoint - the route
# def hello_world():
#     return "<p>Hello, World!</p>"

app.register_blueprint(site)  # pass in site blueprint object to register  <--- registering the blueprint here
app.register_blueprint(auth)
app.register_blueprint(api)  # remember! - need this to get Insomnia token


# instantiate our database & wrap our app in it
db.init_app(app)
migrate = Migrate(app, db)  # things we are connecting/migrating (our application to our database)
app.json_encoder = JSONEncoder  # we are not instantiating this but rather pointing to this class so dont need () at the end
cors = CORS(app)  # Cross Origin Resource Sharing (CORS) aka allowing other apps to talk to our API




