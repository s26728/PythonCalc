import pytest
from calculator import Calculator
from parser import Parser


def test_addition():
    expression = "5 + 5 + 1"
    parser = Parser()
    calculator = Calculator()
    assert calculator.solve(parser.parse(expression)) == 11


def test_subtraction():
    expression = "8 - 3 - 2"
    parser = Parser()
    calculator = Calculator()
    assert calculator.solve(parser.parse(expression)) == 3


def test_multiplication():
    expression = "5 * 5 * 2"
    parser = Parser()
    calculator = Calculator()
    assert calculator.solve(parser.parse(expression)) == 50


def test_division():
    expression = "50 / 2 / 5"
    parser = Parser()
    calculator = Calculator()
    assert calculator.solve(parser.parse(expression)) == 5


def test_root():
    expression = "√36"
    parser = Parser()
    calculator = Calculator()
    assert calculator.solve(parser.parse(expression)) == 6


def test_logarithm():
    expression = "log100"
    parser = Parser()
    calculator = Calculator()
    assert calculator.solve(parser.parse(expression)) == 2


def test_perform():
    calculator = Calculator()
    assert calculator.perform("1", "+", "5") == "6.0"


def test_perform_special():
    calculator = Calculator()
    assert calculator.perform_special("√", "25") == "5.0"


def test_solver_general():
    expression = "12+3*9/2+88/2+2+5"
    parser = Parser()
    calculator = Calculator()
    assert calculator.solve(parser.parse(expression)) == 76.5


def test_solver_brackets():
    expression = "5+(6/(1+3)-55/(10-5))"
    parser = Parser()
    calculator = Calculator()
    assert calculator.solve(parser.parse(expression)) == -4.5


def test_parser():
    expression = "-1+55.5-log2+√36+(34-1)+(-1+(3+7))"
    parser = Parser()
    assert parser.parse(expression) == ["-1", "+", "55.5", "-", "log", "2", "+", "√", "36", "+", "(",
                                        "34", "-", "1", ")", "+", "(", "-1", "+", "(", "3", "+", "7", ")", ")"]


def test_number_check():
    parser = Parser()
    assert (parser.number_check(1) and not parser.number_check("abd"))
