from flask import Flask, render_template, redirect, url_for, request
from datetime import datetime
import os
import json

app = Flask(__name__)
password = os.environ.get("PASSWORD")

@app.route('/')
def landing():
    baseUri = request.args.get('linkingUri')
    return render_template('index.html', time = datetime.now(), linkingUri = baseUri)

@app.route('/login', methods=['POST', 'GET'])
def login():
    baseUri = request.args.get('linkingUri')
    if request.method == 'POST':
        if request.form['password'] == password:
            return redirect(baseUri + 'message=fumichael')
        return redirect(url_for('landing'))
    return redirect(url_for('landing'))
