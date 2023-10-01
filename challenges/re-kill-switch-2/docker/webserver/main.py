from flask import Flask, render_template, request, abort, make_response, current_app
import subprocess
import os
import logging

flag = ''

def check_code(code: str):
    result = subprocess.run(['python3', 'validate.py', code], capture_output=True, text=True)
    return True if result.stdout.find('true') > -1 else False

def start():
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def index():
        return current_app.send_static_file('index.html')

    @app.route(f'/deactivate', methods=['POST'])
    def deactivate():
        if request.json['key']:
            if (check_code(request.json['key'])):
                response = make_response(f'Success code: {flag}', 200)
                response.mimetype = 'application/json'
                return response
            else:
                abort(401)

        abort(400)

    app.run(host='0.0.0.0', port=80, debug=True, use_reloader=False)
flag = os.getenv("FLAG") if os.getenv("FLAG") else "ERROR: FLAG NOT SET"
start()
