from flask import Flask, render_template_string, render_template, jsonify, request, redirect, url_for, session
from flask import render_template
from flask import json
from tester.runner import run_tests
from storage import save_run, list_runs, list_runs_json
from urllib.request import urlopen
from werkzeug.utils import secure_filename
import sqlite3


app = Flask(__name__)


@app.get("/")
def consignes():
    return render_template("consignes.html")


@app.route("/run")
def run():
    result = run_tests()
    save_run(result)
    return jsonify(result)


@app.route("/health")
def health():
    runs = list_runs()
    last = runs[0] if runs else None
    return jsonify({
        "status": "ok",
        "last_run": last.timestamp if last else None,
        "last_availability": last.availability if last else None
    })


@app.route("/dashboard")
def dashboard():
    runs = list_runs()
    last_run = runs[0] if runs else None
    return render_template(
        "dashboard.html",
        runs=runs,
        last_run=last_run
    )


@app.route("/dashboard-json")
def dashboard_json():
    return jsonify(list_runs_json())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
