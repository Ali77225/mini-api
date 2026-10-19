import pytest

from app.erreurs import LIMITE_FACTORIELLE
from app.outils.math import est_premier, factorielle


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


def test_est_premier_3():
    assert est_premier(3)

def test_est_premier_8():
    assert not est_premier(8)

def test_est_premier_2():
    assert est_premier(2)

def test_est_premier_1():
    assert not est_premier(1)

def test_est_premier_0():
    assert not est_premier(0)

def test_est_premier_negatif():
    assert not est_premier(-3)

def test_est_premier_carre():
    assert not est_premier(9)




