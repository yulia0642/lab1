import pytest

from toolkit.errors import CalculatorError
from toolkit.tokenizer import tokenize


def test_tokenize_integer():
    assert tokenize("25") == [
        ("NUMBER", "25"),
    ]


def test_tokenize_expression():
    assert tokenize("2+3*4") == [
        ("NUMBER", "2"),
        ("OP", "+"),
        ("NUMBER", "3"),
        ("OP", "*"),
        ("NUMBER", "4"),
    ]


def test_tokenize_spaces():
    assert tokenize(" 2 + 3 ") == [
        ("NUMBER", "2"),
        ("OP", "+"),
        ("NUMBER", "3"),
    ]


def test_tokenize_unary_minus():
    assert tokenize("2 * -3") == [
        ("NUMBER", "2"),
        ("OP", "*"),
        ("OP", "-"),
        ("NUMBER", "3"),
    ]


def test_empty_expression():
    with pytest.raises(CalculatorError):
        tokenize("")


def test_invalid_character():
    with pytest.raises(CalculatorError):
        tokenize("2+a")


def test_invalid_number():
    with pytest.raises(CalculatorError):
        tokenize("1.2.3")
