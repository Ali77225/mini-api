import pytest

from app.erreurs import LIMITE_FACTORIELLE
from app.outils.math import factorielle


def test_factorielle_de_5():
    assert factorielle(5) == 120

def test_factorielle_de_0():
    assert factorielle(0) == 1

def test_factorielle_de_LIMITE_FACTORIELLE():
    assert factorielle(LIMITE_FACTORIELLE) == LIMITE_FACTORIELLE * factorielle(LIMITE_FACTORIELLE-1)

def test_factorielle_negative():
    with pytest.raises(ValueError):
        factorielle(-1)

def test_factorielle_hors_limite():
    with pytest.raises(ValueError):
        factorielle(LIMITE_FACTORIELLE + 1)
