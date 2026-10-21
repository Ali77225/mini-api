import pytest

from app.erreurs import ConversionErreur
from app.outils.conversion import celsius_fahrenheit


def test_celsius_fahrenheit_normal():
    assert celsius_fahrenheit(0.0) == 32.0
    assert celsius_fahrenheit(100.0) == 212.0
    assert celsius_fahrenheit(-40.0) == -40.0


def test_celsius_fahrenheit_limite():
    assert celsius_fahrenheit(-273.15) == -459.67


def test_celsius_fahrenheit_erreur():
    with pytest.raises(ConversionErreur):
        celsius_fahrenheit(-273.16)