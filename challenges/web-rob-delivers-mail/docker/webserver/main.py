from flask import Flask, render_template, request, abort, make_response, current_app
import subprocess
import os
import logging

flag = ''

def check_grade(input: dict):
    grades = {"Ethan": "A+", "Noah": "A+", "Cody": "A+", "Anthony": "A+"}
    for grade in grades.items():
        if(grade not in input.items()):
            return False
    return True

def check_cookie(input: dict):
    return ("Cookie","c60bd23c9022fe5dd8fa8837036ec9789a27e28666ae5a54606f275451383c89") in input.items()

def start():
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def index():
        return current_app.send_static_file('index.html')

    @app.route('/updateTheGradesB', methods=['POST'])
    def updateGrades():
        if(request.json):
            
            if("c60bd23c9022fe5dd8fa8837036ec9789a27e28666ae5a54606f275451383c89" in request.cookies.values()):
                if (check_grade(request.json)):
                    response = make_response(f'Success code: {flag}', 200)
                    response.mimetype = 'application/json'
                    return response

                abort(404, "User and User Grades do not match")
            abort(401)
        abort(400)

    @app.route('/Help', methods=['GET'])
    def help():
        if("c60bd23c9022fe5dd8fa8837036ec9789a27e28666ae5a54606f275451383c89" in request.cookies.values()):
            return current_app.send_static_file('help.txt')
        abort(401)
     

    app.run(host='0.0.0.0', port=80, debug=True, use_reloader=False)
flag = os.getenv("FLAG") if os.getenv("FLAG") else "ERROR: FLAG NOT SET"
start()
