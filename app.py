from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

def validate_input(input_value):
    try:
        number = int(input_value)
        return number >= 0
    except ValueError:
        return False

@app.route("/triangle")
def generate_triangle():
    input_value = request.args.get('input')
    if not validate_input(input_value):
        return "Invalid Page", 400
    
    result = ''
    for i in range(len(input_value)):
        result += input_value[i] + ('0' * (i+1))  + '<br/>'
    return result

@app.route("/odd")
def generate_odd():
    input_value = request.args.get('input')
    if not validate_input(input_value):
        return "Invalid Page", 400
    
    result = ''
    for i in range(int(input_value) + 1):
        if not i & 1:
            result += str(i) + ' '

    return '<div>' + result + '</div>';

def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
    return True

@app.route("/prime")
def generate_prime():
    input_value = request.args.get('input')
    if not validate_input(input_value):
        return "Invalid Page", 400
    
    result = ''
    for i in range(2, int(input_value) + 1):
        if is_prime(i):
            result += str(i) + ' '
    return '<div>' + result + '</div>';

