#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<string:parameter>")
def print_string(parameter):
    print(parameter)
    return parameter

@app.route("/count/<int:parameter>")
def count(parameter):
    message = "".join([f"{i}\n" for i in range(parameter)])
    return message

@app.route("/math/<num1>/<operation>/<num2>")
def math(num1, operation, num2):
    if not isinstance(num1, int):
        num1 = int(num1)
    if not isinstance(num2, int):
        num2 = int(num2)

    operations = {
        "+": num1 + num2,
        "-": num1 - num2,
        "*": num1 * num2,
        "div": num1 / num2,
        "%": num1 % num2
    }
    result = operations[operation]
    return str(result)

if __name__ == '__main__':
    math(5, "-", 5)
    app.run(port=5555, debug=True)
