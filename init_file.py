
import email
from enum import unique
from importlib.metadata import requires
from flask import Flask, render_template,request,session,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
import random
import sendmail
import math
from html.parser import HTMLParser


UPLOAD_FOLDER='static/uploads/'
app = Flask(__name__)
app.config['SECRET_KEY'] = 'subrahmanya123' 
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
local_server = True
with open("config.json","r") as c:
     param = json.load(c)["param"]


if local_server:
     app.config['SQLALCHEMY_DATABASE_URI'] = param["local_url"]
else:
     app.config['SQLALCHEMY_DATABASE_URI'] = param["prod_url"]
db = SQLAlchemy(app)