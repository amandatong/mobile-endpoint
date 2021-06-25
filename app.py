from flask import Flask, render_template, redirect, url_for, request
from datetime import datetime
import os
import json

app = Flask(__name__)
password = os.environ.get("PASSWORD")

@app.route('/')
def landing():
    return render_template('index.html', time = datetime.now())

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['password'] == password:
            return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
        return redirect(url_for('landing'))
    return redirect(url_for('landing'))