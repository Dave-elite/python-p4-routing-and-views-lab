#!/usr/bin/env python3

from flask import Flask
from flask import escape

app = Flask(__name__)

@app.route('/')
def index():
        return f"<h1>Python Operations with Flask Routing and Views</h1>"
    
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  # This should print to console
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = "\n".join(str(i) for i in range(parameter))  # Generate numbers from 0 to parameter-1
    return numbers + '\n'  # Ensure it ends with a newline



@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    try: 
        if operation == '+':
            return f"{num1 + num2}"
        elif operation == '-':
            return f"{num1 - num2}"
        elif operation == '*':
            return f"{num1 * num2}"
        elif operation == 'div':
            if num2 == 0:
                return "Cannot divide by zero"
            return f"{num1 / num2}"
        elif operation == '%':
            return f"{num1 % num2}"
        else:
            return "Invalid operation"
    except ValueError:
        return "Invalid input, please enter integers only"



if __name__ == '__main__':
    app.run(port=5555, debug=True)
