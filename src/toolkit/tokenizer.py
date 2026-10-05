from toolkit.errors import CalculatorError

Token = tuple[str, str]


def tokenize(expression: str) -> list[Token]:
    """Convert an arithmetic expression into a list of tokens."""

    if expression.strip() == "":
        raise CalculatorError("empty expression")

    tokens = []
    i = 0

    while i < len(expression):
        character = expression[i]

        if character.isspace():
            i += 1
            continue

        if character in "+-*/":
            tokens.append(("OP", character))
            i += 1
            continue

        if character.isdigit() or character == ".":
            start = i
            dot_count = 0

            while i < len(expression):
                character = expression[i]

                if character.isdigit():
                    i += 1
                    continue

                if character == ".":
                    dot_count += 1

                    if dot_count > 1:
                        raise CalculatorError("invalid number")

                    i += 1
                    continue

                break

            number = expression[start:i]

            if number == ".":
                raise CalculatorError("invalid number")

            tokens.append(("NUMBER", number))
            continue

        raise CalculatorError(f"invalid character: {character}")

    return tokens
