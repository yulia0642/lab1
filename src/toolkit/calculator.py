from toolkit.errors import CalculatorError, DivisionByZeroError
from toolkit.tokenizer import Token, tokenize


def calculate(expression: str) -> float:
    """Calculate an arithmetic expression."""

    tokens = tokenize(expression)
    tokens = handle_unary_signs(tokens)
    validate_tokens(tokens)

    return evaluate_tokens(tokens)


def handle_unary_signs(tokens: list[Token]) -> list[Token]:
    """Convert unary signs into signed number tokens."""

    result = []
    i = 0
    expect_number = True

    while i < len(tokens):
        token_type, value = tokens[i]

        if expect_number and token_type == "OP" and value in "+-":
            if i + 1 >= len(tokens):
                raise CalculatorError("missing operand")

            next_type, next_value = tokens[i + 1]

            if next_type != "NUMBER":
                raise CalculatorError("missing operand")

            if value == "-":
                next_value = "-" + next_value

            result.append(("NUMBER", next_value))
            expect_number = False
            i += 2
            continue

        result.append(tokens[i])

        if token_type == "NUMBER":
            expect_number = False
        else:
            expect_number = True

        i += 1

    return result


def validate_tokens(tokens: list[Token]) -> None:
    """Check that numbers and operators are in the correct order."""

    if not tokens:
        raise CalculatorError("empty expression")

    expect_number = True

    for token_type, value in tokens:
        if expect_number:
            if token_type != "NUMBER":
                raise CalculatorError("missing operand")
        else:
            if token_type != "OP":
                raise CalculatorError("missing operator")

        expect_number = not expect_number

    if expect_number:
        raise CalculatorError("missing operand")


def evaluate_tokens(tokens: list[Token]) -> float:
    """Calculate a validated list of tokens."""

    if not tokens:
        raise CalculatorError("empty expression")

    numbers = [float(tokens[0][1])]
    operators = []

    i = 1

    while i < len(tokens):
        operator = tokens[i][1]
        value = float(tokens[i + 1][1])

        if operator == "*":
            numbers[-1] *= value

        elif operator == "/":
            if value == 0:
                raise DivisionByZeroError("division by zero")

            numbers[-1] /= value

        else:
            operators.append(operator)
            numbers.append(value)

        i += 2

    result = numbers[0]

    for i in range(len(operators)):
        operator = operators[i]
        value = numbers[i + 1]

        if operator == "+":
            result += value
        else:
            result -= value

    return result
