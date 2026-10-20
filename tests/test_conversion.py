import pytest

from app.erreurs import ConversionErreur
from app.outils.conversion import celsius_fahrenheit, euros_devise


def test_euros_devise_normal():
    assert euros_devise(100.0, "USD") == 108.0


def test_euros_devise_limite():
    assert euros_devise(0.0, "GBP") == 0.0


def test_euros_devise_erreur():
    with pytest.raises(ConversionErreur):
        euros_devise(-10.0, "USD")
    with pytest.raises(ConversionErreur):
        euros_devise(50.0, "INCONNUE")


def test_celsius_fahrenheit_normal():
    assert celsius_fahrenheit(0.0) == 32.0
    assert celsius_fahrenheit(100.0) == 212.0
    assert celsius_fahrenheit(-40.0) == -40.0


def test_celsius_fahrenheit_limite():
    assert celsius_fahrenheit(-273.15) == -459.67


def test_celsius_fahrenheit_erreur():
    with pytest.raises(ConversionErreur):
        celsius_fahrenheit(-273.16)