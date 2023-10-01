from flask import Flask, render_template, request, abort, make_response, current_app
import subprocess
import os
import logging
import secrets
import string

flag = ''

def start():
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def index():
        return current_app.send_static_file('index.html')

    @app.route(f'/message', methods=['GET'])
    def realMessage():
        response = make_response(f'Success code: {flag}', 200)
        response.mimetype = 'application/json'
        return response
          
    @app.route(f'/message', methods=['POST'])
    def fakeMessage():
        resp = ''.join(secrets.choice(string.ascii_uppercase + string.digits)
              for i in range(25))
        response = make_response(resp, 200)
        response.mimetype = 'application/json'
        return response
    
    app.run(host='0.0.0.0', port=80, debug=True, use_reloader=False)
flag = os.getenv("FLAG") if os.getenv("FLAG") else "ERROR: FLAG NOT SET"
start()
