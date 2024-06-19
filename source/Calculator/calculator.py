class Calculator:

    def __init__(self):
        self.value = 1

    def solve(self, expression):
        while len(expression) != 1:

            count = 0
            while count < len(expression) - 1:
                if expression[count] == "(":
                    if expression[count + 2] == ")":
                        del expression[count + 2]
                        del expression[count]
                count += 1

            count = 0
            while count < len(expression) - 1:
                if (expression[count] in ["*", "/"] and not
                (self.paranthesis_check([count + 1]) or self.paranthesis_check([count - 1]))):
                    expression[count - 1] = self.perform(
                        expression[count - 1], expression[count], expression[count + 1])
                    del expression[count + 1]
                    del expression[count]
                count += 1

            count = 0
            while count < len(expression) - 1:
                if (expression[count] in ["+", "-"] and not
                (self.paranthesis_check([count + 1]) or self.paranthesis_check([count - 1]))):
                    expression[count - 1] = self.perform(
                        expression[count - 1], expression[count], expression[count + 1])
                    del expression[count + 1]
                    del expression[count]
                count += 1

        return float(expression[0])

    def perform(self, n1, operand, n2):
        if operand == "+":
            return str(self.add(float(n1), float(n2)))
        elif operand == "-":
            return str(self.subtract(float(n1), float(n2)))
        elif operand == "*":
            return str(self.multiply(float(n1), float(n2)))
        elif operand == "/":
            return str(self.divide(float(n1), float(n2)))

    def paranthesis_check(self, expression):
        paranthesis_list = ["(", ")"]
        if expression in paranthesis_list:
            return True
        else:
            return False

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero"
