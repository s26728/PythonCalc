from flask import Flask, render_template, request, jsonify
from calculator import Calculator
from parser import Parser

app = Flask(__name__)

calculator = Calculator()
parser = Parser()


@app.route("/calculator")
def calc():
    return render_template("calculator.html")


@app.route("/solve", methods=['GET'])
def solve():
    global calculator
    global parser
    expression = parser.parse(request.args.get('expression'))
    return jsonify({'result': calculator.solve(expression)})


if __name__ == "__main__":
    #app.run()
    expression = "√36"
    print(parser.parse(expression))
    print(calculator.solve(parser.parse(expression)))
    # print(calculator.solve(['log', '(', '4', '*', '3', ')', '+', '(', '3', '/', '2', ')']))
