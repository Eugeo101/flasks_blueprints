from flask import Flask, render_template, redirect, url_for
from flask import request, session
from flask import flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

from admin.second import second

app = Flask("Service Name")
app.register_blueprint(second, url_prefix="/admin")

@app.route("/")
def test():
    return "<h1>Test</h1>"


app.run(debug=True, port=5000)