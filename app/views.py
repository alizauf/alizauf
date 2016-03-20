from flask import render_template, url_for
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/writing')
def writing():
    return render_template('writing.html')

@app.route('/design')
def design():
    return render_template('design.html')

@app.route('/twin-peaks')
def twin_peaks():
    return render_template('twin-peaks.html')
