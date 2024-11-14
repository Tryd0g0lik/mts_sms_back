"""
This is base Flask.
Here is a basis function of flask. That is start
"""
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_wtf import CSRFProtect
from dotenv_ import (PROJECT_HOST,
                     PROJECT_PORT,
                     PROJECT_PROTOCOL,
                     PROJECT_SECRET_KEY)
from flask_bootstrap import Bootstrap
app_sms = Flask(__name__,
                template_folder="templates")
app_sms.config.from_object(__name__)

# CONFIG
app_sms.config["PROJECT_HOST"] = PROJECT_HOST
app_sms.config["PROJECT_PORT"] = PROJECT_PORT
app_sms.config["PROJECT_PROTOCOL"] = PROJECT_PROTOCOL
app_sms.config["PROJECT_SECRET_KEY"] = PROJECT_SECRET_KEY

# CSRF token
csrf = CSRFProtect(app_sms)
# OTHERS
bootstrap = Bootstrap(app_sms)
bcrypt = Bcrypt(app_sms)

app_type = type(app_sms)

