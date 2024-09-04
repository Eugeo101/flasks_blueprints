from flask import Blueprint, render_template, redirect, url_for
from flask import request, session
from flask import flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy


second = Blueprint("admin", __name__, static_folder='static', template_folder='templates')

@second.route("/home")
@second.route("/")
def home():
    return render_template("home.html")