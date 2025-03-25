
import sympy as sp
from flask import Flask, render_template, request

app = Flask(__name__)

# Define symbol
x = sp.symbols('x')

@app.route('/', methods=['GET', 'POST'])
def run():
    result = None
    if request.method == 'POST':
        user_input = request.form['expression']  # Get the user input from the form
        try:
            # Parse the user input and compute the integral
            expr = sp.sympify(user_input)  # Converts string input to SymPy expression
            result = sp.integrate(expr, x)
        except Exception as e:
            result = f"Error: {e}"  # Handle invalid input or errors

    return render_template('results.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
