from flask import Flask, request
from print import do_print

app = Flask(__name__)


@app.route("/")
def hello_world():
    return """
    <!doctype html>
    <head>
    <title>receiptd print server></title>
    <body style='font-family: sans-serif;'>
    <h1>receiptd print server running</h1>
    <p>(c) 2025 Matt Young - ISC licence</p>
    </body>
    """


@app.route("/print/job", methods=["GET"])
def print():
    name = request.args["name"]
    status = request.args["status"]
    hostname = request.args["hostname"]
    log = "none"

    try:
        do_print(name, status, log, hostname)
        return "OK"
    except Exception as e:
        print(f"Failed to print: {e}")
