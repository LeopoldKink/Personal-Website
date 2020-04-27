
import json
import dateutil.parser
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for, send_from_directory, session
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy import desc
import sys
from datetime import datetime, date


app = Flask(__name__)
moment = Moment(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:haha@localhost:5432/design'




@app.route('/packlay')
def packlay():
    return render_template('packlay.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mail')
def mail():
    return render_template('mail.html')

@app.route('/webpack')
def webpack():
    return render_template('webpack.html')

@app.route('/customwebpack')
def custom_webpack():
    return render_template('customwebpack.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/team')
def team():
    return render_template('team.html')

if __name__ == '__main__':
    app.run()

@app.route('/projekte')
def projekte():
    return render_template('projekte.html')