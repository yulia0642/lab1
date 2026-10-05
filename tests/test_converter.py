import pytest

from toolkit.converter import convert
from toolkit.errors import (
    AbsoluteZeroError,
    IncompatibleUnitsError,
    InvalidNumberError,
    UnknownUnitError,
)


def test_millimeters_to_meters():
    assert convert("1000", "mm", "m") == 1.0


def test_kilograms_to_grams():
    assert convert("1.5", "kg", "g") == 1500.0


def test_celsius_to_fahrenheit():
    assert convert("0", "c", "f") == 32.0


def test_celsius_absolute_zero_to_kelvin():
    assert convert("-273.15", "c", "k") == pytest.approx(0.0)


def test_temperature_below_absolute_zero():
    with pytest.raises(AbsoluteZeroError):
        convert("-300", "c", "k")


def test_incompatible_units():
    with pytest.raises(IncompatibleUnitsError):
        convert("1", "kg", "m")


def test_uppercase_units():
    assert convert("1000", "MM", "M") == 1.0


def test_unknown_from_unit():
    with pytest.raises(UnknownUnitError):
        convert("100", "abc", "m")


def test_unknown_to_unit():
    with pytest.raises(UnknownUnitError):
        convert("100", "m", "abc")


def test_invalid_number():
    with pytest.raises(InvalidNumberError):
        convert("abc", "kg", "g")
