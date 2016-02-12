from flask import render_template, url_for
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/twin-peaks')
def twin_peaks():
    return render_template('twin-peaks.html')
