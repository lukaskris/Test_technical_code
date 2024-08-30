from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

def validate_input(input_value):
    """Validates if the input is a non-negative integer."""
    try:
        number = int(input_value)
        return number >= 0
    except ValueError:
        return False

@app.route("/triangle")
def generate_triangle():
    input_value = request.args.get('input')
    if not validate_input(input_value):
        return "Invalid Input", 400
    
    result = ''.join(f"{char}{'0' * (i + 1)}<br/>" for i, char in enumerate(input_value))
    return result

@app.route("/odd")
def generate_odd():
    input_value = request.args.get('input')
    if not validate_input(input_value):
        return "Invalid Input", 400
    
    result = ' '.join(str(i) for i in range(int(input_value) + 1) if i % 2 == 1)
    return f'<div>{result}</div>'

def is_prime(number):
    """Checks if a number is a prime."""
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
        return "Invalid Input", 400
    
    result = ' '.join(str(i) for i in range(2, int(input_value) + 1) if is_prime(i))
    return f'<div>{result}</div>'

if __name__ == "__main__":
    app.run(debug=True)
