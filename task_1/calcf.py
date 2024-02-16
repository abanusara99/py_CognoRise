from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('cal.html', display='', is_calculator_on=True)

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = request.form.get('num1', '')
    num2 = request.form.get('num2', '')
    operation = request.form.get('operation', '')
    is_calculator_on = request.form.get('is_calculator_on', '')

    if is_calculator_on:
        try:
            if operation == '+':
                result = float(num1) + float(num2)
            elif operation == '-':
                result = float(num1) - float(num2)
            elif operation == '*':
                result = float(num1) * float(num2)
            elif operation == '/':
                result = float(num1) / float(num2) if float(num2) != 0 else 'Error: Division by zero'
            else:
                result = 'Invalid operation'
        except ValueError:
            result = 'Error: Invalid input'

    else:
        result = ''

    return render_template('cal.html', display=result, is_calculator_on=is_calculator_on)

if __name__ == '__main__':
    app.run(debug=True)
