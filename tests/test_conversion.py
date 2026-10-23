"""Tests unitaires du module conversion."""

import pytest

from app.erreurs import ConversionErreur
from app.outils.conversion import celsius_fahrenheit, km_mile


def test_celsius_fahrenheit_normal():
    assert celsius_fahrenheit(0.0) == 32.0
    assert celsius_fahrenheit(100.0) == 212.0
    assert celsius_fahrenheit(-40.0) == -40.0


def test_celsius_fahrenheit_limite():
    assert celsius_fahrenheit(-273.15) == -459.67


def test_celsius_fahrenheit_erreur():
    with pytest.raises(ConversionErreur):
        celsius_fahrenheit(-273.16)


def test_km_mile_succes():
    assert km_mile(10.0) == 6.21
    assert km_mile(0.0) == 0.0


def test_km_mile_negatif():
    with pytest.raises(ConversionErreur):
        km_mile(-5.0)
