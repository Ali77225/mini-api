import pytest
from app.outils.conversion import celsius_fahrenheit
from app.erreurs import ConversionErreur


def test_celsius_fahrenheit_normal():
    assert celsius_fahrenheit(0.0) == 32.0


def test_celsius_fahrenheit_limite():
    assert celsius_fahrenheit(-273.15) == -459.67


def test_celsius_fahrenheit_erreur():
    with pytest.raises(ConversionErreur):
        celsius_fahrenheit(-300.0)