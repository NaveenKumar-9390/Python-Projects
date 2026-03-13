def precedence(op):

    if op in ('+', '-'):
        return 1

    if op in ('*', '/'):
        return 2

    return 0


def apply_op(a, b, op):

    if op == '+':
        return a + b

    if op == '-':
        return a - b

    if op == '*':
        return a * b

    if op == '/':
        return a / b


def evaluate(expression):

    values = []
    ops = []

    i = 0

    while i < len(expression):

        if expression[i] == ' ':
            i += 1
            continue

        if expression[i].isdigit():

            val = 0

            while i < len(expression) and expression[i].isdigit():
                val = val * 10 + int(expression[i])
                i += 1

            values.append(val)
            continue

        elif expression[i] == '(':
            ops.append(expression[i])

        elif expression[i] == ')':

            while ops and ops[-1] != '(':

                b = values.pop()
                a = values.pop()
                op = ops.pop()

                values.append(apply_op(a, b, op))

            ops.pop()

        else:

            while (ops and precedence(ops[-1]) >= precedence(expression[i])):

                b = values.pop()
                a = values.pop()
                op = ops.pop()

                values.append(apply_op(a, b, op))

            ops.append(expression[i])

        i += 1

    while ops:

        b = values.pop()
        a = values.pop()
        op = ops.pop()

        values.append(apply_op(a, b, op))

    return values[0]


def main():

    while True:

        expr = input("\nEnter expression (or exit): ")

        if expr == "exit":
            break

        result = evaluate(expr)

        print("Result:", result)


if __name__ == "__main__":
    main()
