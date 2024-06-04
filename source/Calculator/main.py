from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/calculator")
def calc():
    return render_template('calculator.html')


if __name__ == "__main__":
    app.run()
