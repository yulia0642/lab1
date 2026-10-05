import pytest

from toolkit.calculator import calculate
from toolkit.errors import CalculatorError, DivisionByZeroError


def test_addition_with_precedence():
    assert calculate("2+3*4") == 14.0


def test_division():
    assert calculate("10 / 4") == 2.5


def test_multiplication_with_unary_minus():
    assert calculate("2 * -3") == -6.0


def test_addition_with_unary_minus():
    assert calculate("1+-2") == -1.0


def test_empty_expression():
    with pytest.raises(CalculatorError):
        calculate("")


def test_two_binary_operators():
    with pytest.raises(CalculatorError):
        calculate("2*/3")


def test_invalid_character():
    with pytest.raises(CalculatorError):
        calculate("2+a")


def test_division_by_zero():
    with pytest.raises(DivisionByZeroError):
        calculate("1/0")


def test_subtraction():
    assert calculate("7-3") == 4.0


def test_multiplication():
    assert calculate("2*3") == 6.0


def test_unary_minus_at_start():
    assert calculate("-5") == -5.0


def test_unary_plus():
    assert calculate("+5") == 5.0


def test_missing_operand():
    with pytest.raises(CalculatorError):
        calculate("2+")


def test_missing_operator():
    with pytest.raises(CalculatorError):
        calculate("2 3")


def test_invalid_number():
    with pytest.raises(CalculatorError):
        calculate("1.2.3")
