from flask import Flask, render_template_string, render_template, jsonify, request, redirect, url_for, session
from flask import render_template
from flask import json
from tester.runner import run_tests
from storage import save_run, list_runs
from urllib.request import urlopen
from werkzeug.utils import secure_filename
import sqlite3

app = Flask(__name__)

@app.get("/")
def consignes():
     return render_template('consignes.html')


@app.route("/run")
def run():

    result = run_tests()

    save_run(result)

    return jsonify(result)

@app.route("/health")
def health():

    return {"status": "ok"}

@app.route("/dashboard")
def dashboard():

    runs = list_runs()

    return render_template("dashboard.html", runs=runs)

if __name__ == "__main__":
    # utile en local uniquement
    app.run(host="0.0.0.0", port=5000, debug=True)
