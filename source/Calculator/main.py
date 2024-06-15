from flask import Flask, render_template, request
from calculator import Calculator

app = Flask(__name__)

calculator = Calculator()

@app.route("/calculator")
def calc():
    global calculator
    return render_template("calculator.html", value=calculator.value)


if __name__ == "__main__":
    app.run()
