import math

class Calculator:
    def solve(self, expression):
        while len(expression) != 1:

            # Solving the brackets
            count = 0
            while count < len(expression):
                if expression[count] == "(":
                    print(expression)

                    parenthesis_1_pos = count
                    parenthesis_2_pos = 0

                    inner_count = 0
                    paranthesis_2_set = False
                    while inner_count < len(expression):
                        if expression[inner_count] == "(":
                            if paranthesis_2_set == False:
                                parenthesis_1_pos = inner_count
                        if expression[inner_count] == ")":
                            parenthesis_2_pos = inner_count
                            paranthesis_2_set = True
                            break
                        inner_count += 1

                    expression[parenthesis_1_pos] = self.solve(expression[parenthesis_1_pos+1:parenthesis_2_pos])
                    del expression[parenthesis_1_pos+1:parenthesis_2_pos+1]

                    count = 0
                count += 1

            # Logarithms
            count = 0
            while count < len(expression) - 1:
                if (expression[count] in ["log"] and not (
                        self.parenthesis_check([count + 1]) or self.parenthesis_check([count - 1]))):
                    expression[count] = self.perform_special(
                        expression[count], expression[count + 1])
                    del expression[count + 1]
                count += 1

            # Multiplication and division
            count = 0
            while count < len(expression) - 1:
                if (expression[count] in ["*", "/"] and not (
                        self.parenthesis_check([count + 1]) or self.parenthesis_check([count - 1]))):
                    expression[count - 1] = self.perform(
                        expression[count - 1], expression[count], expression[count + 1])
                    del expression[count + 1]
                    del expression[count]
                count += 1

            # Addition and subtraction
            count = 0
            while count < len(expression) - 1:
                if (expression[count] in ["+", "-"] and not (
                        self.parenthesis_check([count + 1]) or self.parenthesis_check([count - 1]))):
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

    def perform_special(self, fun, n1):
        if fun == "log":
            return self.logarithm(n1)

    def parenthesis_check(self, expression):
        parenthesis_list = ["(", ")"]
        if expression in parenthesis_list:
            return True
        else:
            return False

    def brackets_check(self, expression):
        print("haha")


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

    def logarithm(self, x):
        return math.log10(x)
