class Parser:
    def number_check(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def list_convert(self, input_expression):
        input_expression = input_expression.replace(" ", "")
        output_list = []
        for element in input_expression:
            output_list.append(element)
        count = 0
        while count < len(output_list) - 1:
            if self.number_check(output_list[count]) and self.number_check(output_list[count + 1]):
                output_list[count] += output_list[count + 1]
                del output_list[count + 1]
            elif self.number_check(output_list[count]) and output_list[count + 1] == ".":
                if self.number_check(output_list[count + 2]):
                    output_list[count] += output_list[count + 1] + output_list[count + 2]
                    del output_list[count + 2]
                    del output_list[count + 1]
            else:
                count += 1
        return output_list

    def parse(self, input_expression):
        return self.list_convert(input_expression)
