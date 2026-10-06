from toolkit.constants import LENGTH_TO_METERS, MASS_TO_GRAMS, UNIT_GROUPS
from toolkit.errors import (
    AbsoluteZeroError,
    IncompatibleUnitsError,
    InvalidNumberError,
    UnknownUnitError,
)


def convert(value: str, from_unit: str, to_unit: str) -> float:
    """Convert a value from one unit to another."""

    from_unit = from_unit.strip().lower()
    to_unit = to_unit.strip().lower()

    if from_unit not in UNIT_GROUPS:
        raise UnknownUnitError(f"unknown unit: {from_unit}")

    if to_unit not in UNIT_GROUPS:
        raise UnknownUnitError(f"unknown unit: {to_unit}")

    if UNIT_GROUPS[from_unit] != UNIT_GROUPS[to_unit]:
        raise IncompatibleUnitsError(
            f"incompatible units: {from_unit} and {to_unit}"
        )

    try:
        number = float(value)
    except ValueError:
        raise InvalidNumberError(f"invalid number: {value}")

    group = UNIT_GROUPS[from_unit]

    if group == "length":
        return convert_length(number, from_unit, to_unit)

    if group == "mass":
        return convert_mass(number, from_unit, to_unit)

    return convert_temperature(number, from_unit, to_unit)


def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    """Convert a length value."""

    value_in_meters = value * LENGTH_TO_METERS[from_unit]
    return value_in_meters / LENGTH_TO_METERS[to_unit]


def convert_mass(value: float, from_unit: str, to_unit: str) -> float:
    """Convert a mass value."""

    value_in_grams = value * MASS_TO_GRAMS[from_unit]
    return value_in_grams / MASS_TO_GRAMS[to_unit]


def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    """Convert a temperature value."""

    kelvin = to_kelvin(value, from_unit)

    if kelvin < 0:
        raise AbsoluteZeroError("temperature is below absolute zero")

    return from_kelvin(kelvin, to_unit)


def to_kelvin(value: float, unit: str) -> float:
    """Convert a temperature to Kelvin."""

    if unit == "c":
        return value + 273.15

    if unit == "f":
        return (value - 32) * 5 / 9 + 273.15

    return value


def from_kelvin(value: float, unit: str) -> float:
    """Convert Kelvin to the target temperature unit."""

    if unit == "c":
        return value - 273.15

    if unit == "f":
        return (value - 273.15) * 9 / 5 + 32

    return value
