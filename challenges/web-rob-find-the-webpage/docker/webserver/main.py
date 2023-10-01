from flask import Flask, render_template, request, abort, make_response, current_app
import subprocess
import os
import logging

def start():
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def index():
        return current_app.send_static_file('index.html')

    @app.route('/viewGrades', methods=['GET'])
    def viewGrades():
        return current_app.send_static_file('viewGrades.html')

    app.run(host='0.0.0.0', port=80, debug=True, use_reloader=False)
start()
