class ToolkitError(Exception):
    """Base class for errors in the toolkit."""


class CalculatorError(ToolkitError):
    """Error in an arithmetic expression."""


class DivisionByZeroError(CalculatorError):
    """Division by zero was requested."""


class ConversionError(ToolkitError):
    """Error in a unit conversion."""


class UnknownUnitError(ConversionError):
    """The specified unit is unknown."""


class IncompatibleUnitsError(ConversionError):
    """The source and target units belong to different groups."""


class AbsoluteZeroError(ConversionError):
    """The temperature is below absolute zero."""


class InvalidNumberError(ConversionError):
    """The specified value is not a valid number."""
