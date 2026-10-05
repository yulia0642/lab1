import subprocess
import sys


def test_help():
    result = subprocess.run(
        [sys.executable, "-m", "toolkit", "--help"],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert "Calculator and unit converter" in result.stdout


def test_short_help():
    result = subprocess.run(
        [sys.executable, "-m", "toolkit", "-help"],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0


def test_calculator_cli():
    result = subprocess.run(
        [sys.executable, "-m", "toolkit", "calc", "2+3*4"],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert result.stdout.strip() == "14.0"
    assert result.stderr == ""


def test_calculator_error_cli():
    result = subprocess.run(
        [sys.executable, "-m", "toolkit", "calc", "1/0"],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 2
    assert result.stderr != ""
    assert result.stdout == ""


def test_converter_cli():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "toolkit",
            "convert",
            "1000",
            "--from",
            "mm",
            "--to",
            "m",
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert result.stdout.strip() == "1.0"
    assert result.stderr == ""


def test_incompatible_units_cli():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "toolkit",
            "convert",
            "1",
            "--from",
            "kg",
            "--to",
            "m",
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 2
    assert result.stderr != ""
    assert result.stdout == ""
