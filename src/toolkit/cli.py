import argparse
import sys

from toolkit.calculator import calculate
from toolkit.converter import convert
from toolkit.errors import ToolkitError


def main() -> int:
    """Run the command-line interface."""

    parser = argparse.ArgumentParser(
        prog="toolkit",
        description="Calculator and unit converter",
    )

    parser.add_argument(
        "-help",
        action="help",
        help="Show this help message and exit",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    calc_parser = subparsers.add_parser(
        "calc",
        help="Calculate an arithmetic expression",
    )

    calc_parser.add_argument(
        "expression",
        help="Arithmetic expression",
    )

    convert_parser = subparsers.add_parser(
        "convert",
        help="Convert a value between units",
    )

    convert_parser.add_argument(
        "value",
        help="Value to convert",
    )

    convert_parser.add_argument(
        "--from",
        dest="from_unit",
        required=True,
        help="Source unit",
    )

    convert_parser.add_argument(
        "--to",
        dest="to_unit",
        required=True,
        help="Target unit",
    )

    args = parser.parse_args()

    try:
        if args.command == "calc":
            result = calculate(args.expression)
            print(result)

        elif args.command == "convert":
            result = convert(
                args.value,
                args.from_unit,
                args.to_unit,
            )
            print(result)

    except ToolkitError as error:
        print(error, file=sys.stderr)
        return 2

    return 0
