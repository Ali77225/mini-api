import pytest

from app.erreurs import DEVISE_NON_SUPPORTEE_FINANCE, MONTANT_NEGATIF_FINANCE
from app.outils.finance import FinanceErreur, euro_devise


def test_euro_devise_succes():
    assert euro_devise(100.0, "USD") == 108.0
    assert euro_devise(50.0, "gbp") == 42.5


def test_euro_devise_montant_zero():
    assert euro_devise(0.0, "USD") == 0.0


def test_euro_devise_montant_negatif():
    with pytest.raises(FinanceErreur, match=MONTANT_NEGATIF_FINANCE):
        euro_devise(-10.0, "USD")


def test_euro_devise_inconnue():
    with pytest.raises(FinanceErreur, match=DEVISE_NON_SUPPORTEE_FINANCE):
        euro_devise(100.0, "XYZ")
