from flask import Flask, render_template, request, abort, make_response, current_app
import subprocess
import os
import logging

flag = ''

def check_code(code: str):
    users = ["GPT", "Bard", "DALL-E", "DeepBrain" , "JASPER", "Midjourney" , "Sam the Intern"]
    print(code)
    for u in users:
        if(u not in code):
            return False
    
    return True

def start():
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def index():
        return current_app.send_static_file('index.html')

    @app.route('/users', methods=['DELETE'])
    def delete():
        if(request.data):
            if (check_code(request.data.decode("UTF-8"))):
                
                response = make_response(f'Success code: {flag}', 200)
                response.mimetype = 'application/json'
                return response
            else:
                abort(401)

        abort(400)

    app.run(host='0.0.0.0', port=80, debug=True, use_reloader=False)
flag = os.getenv("FLAG") if os.getenv("FLAG") else "ERROR: FLAG NOT SET"
start()
