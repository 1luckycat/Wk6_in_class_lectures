# our configuration file which configures our flask app aka tells it all the specific details
# it needs to know about this specific app via variables

from datetime import timedelta
import os # operating system necessary for python applications so python can be interpreted on any os
#  meaning it will work on anyone's computer
from dotenv import load_dotenv # allows us to load our environment variables from a different file 
# (so we can secure them)

# establish our base directory so when we use "." in our app it knows that rangers_shop is our base dir
basedir = os.path.abspath(os.path.dirname(__file__))  # this part is used to know it goes to rangers_shop

# establish where our enviroment variables are coming from
load_dotenv(os.path.join(basedir, '.env'))  # this is saying looking into this file for our env variables


# create our Config class
class Config():

    """
    Create Config class which will setup our configuration variables.
    Using environment variables where available otherwise create config variables.
    """

    FLASK_APP = os.environ.get('FLASK_APP') # looking for key of FLASK_APP in .env file
    FLASK_ENV = os.environ.get('FLASK_ENV')
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Literally can be whatever you want' # usually a string
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')  # if any issues, will default to this path
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # we dont want a message every single time our database changes  -- not in notation
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=365)
    
