from flask import Flask, render_template, request, jsonify
from calculator import Calculator
from parser import Parser

app = Flask(__name__)

calculator = Calculator()
parser = Parser()


@app.route("/calculator")
def calc():
    global calculator
    return render_template("calculator.html", value=calculator.value)


@app.route("/addition", methods=['GET'])
def solve():
    global calculator
    global parser
    x = int(request.args.get('x'))
    y = int(request.args.get('y'))
    return jsonify({'result': calculator.add(x, y)})


if __name__ == "__main__":
    # app.run()
    print(calculator.solve(parser.parse("1+1+2.2*33.266+4+5+6+7+8")))
