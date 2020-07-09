from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

#This first loads the configuration from the yourapplication.default_settings module and
#then overrides the values with the contents of the file the YOURAPPLICATION_SETTINGS environment variable points to. This environment variable can be set on Linux 
#or OS X with the export command in the shell before starting the server:

app.config.from_object('app.default_settings')
app.config.from_envvar('FLASK_CONFIG')


#app.config.from_object('app.default_settings')
#app.config.from_envvar('APP_SETTINGS')

#db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True)