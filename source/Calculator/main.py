from flask import Flask, render_template, request, jsonify
from calculator import Calculator

app = Flask(__name__)

calculator = Calculator()


@app.route("/calculator")
def calc():
    global calculator
    return render_template("calculator.html", value=calculator.value)


@app.route("/addition", methods=['GET'])
def addition():
    global calculator
    x = int(request.args.get('x'))
    y = int(request.args.get('y'))
    return jsonify({'result': calculator.add(x, y)})


if __name__ == "__main__":
    app.run()
