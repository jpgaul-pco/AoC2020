from operator import add, mul
import re

lines = []
rounds = 6
offset = rounds + 1
operator_map = {"+": add, "*": mul}


def read_file():
    file = open("input.txt", "r")
    [lines.append(line.strip()) for line in file]
    file.close()


def get_between_parenths(line_array):
    stack = 1
    for idx, elem in enumerate(line_array):
        if elem == "(":
            stack += 1
        elif elem == ")":
            stack -= 1
        if stack == 0:
            return line_array[:idx], line_array[idx + 1:]
    return [], []


def new_hoo_hoo_math(line_array):
    num = 0
    operator = "+"
    while line_array:
        token = line_array.pop(0)
        if token == "(":
            inner_array, line_array = get_between_parenths(line_array)
            token = new_hoo_hoo_math(inner_array)
        if token in ["+", "*"]:
            operator = token
        else:
            num = operator_map[operator](num, int(token))

    return num


def shunt_yard_algo(line_array):
    priority_map = {")": -1, "(": -1, "+": 3, "*": 1}
    out_stack = []
    operator_stack = []
    for token in line_array:
        if token.isnumeric():
            out_stack.append(int(token))
        elif token in ["+", "*"]:
            while operator_stack and priority_map[token] <= priority_map[operator_stack[-1]] and operator_stack[-1] != "(":
                out_stack.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == "(":
            operator_stack.append(token)
        elif token == ")":
            while operator_stack[-1] != "(":
                out_stack.append(operator_stack.pop())
            operator_stack.pop()

    while operator_stack:
        out_stack.append(operator_stack.pop())

    return out_stack


def eval_RPN(tokens):
    rev_tokens = []
    for token in tokens:
        if token in ["+", "*"]:
            token = operator_map[token](rev_tokens.pop(), rev_tokens.pop())
        rev_tokens.append(token)
    return rev_tokens.pop()


def main():
    read_file()
    output = sum([new_hoo_hoo_math(re.findall(r"\+|\*|\(|\)|\d", line)) for line in lines])
    fancy_output = sum([eval_RPN(shunt_yard_algo(re.findall(r"\+|\*|\(|\)|\d", line))) for line in lines])

    print(f"The sum of all problems is {output}")
    print(f"The sum of all harder problems is {fancy_output}")


if __name__ == "__main__":
    main()
