import pytest
from fastapi.testclient import TestClient

from app.erreurs import ConversionErreur
from app.main import app
from app.outils.conversion import km_miles

client = TestClient(app)


def test_km_miles_normal():
    assert km_miles(10.0) == 6.2137


def test_km_miles_limite():
    assert km_miles(0.0) == 0.0


def test_km_miles_erreur():
    with pytest.raises(ConversionErreur):
        km_miles(-5.0)


def test_sante():
    r = client.get("/sante")
    assert r.status_code == 200
    assert r.json() == {"statut": "ok"}


def test_conversion_celsius_fahrenheit():
    r = client.get("/celsius-fahrenheit", params={"celsius": 0})
    assert r.status_code == 200
    assert r.json() == {"celsius": 0.0, "fahrenheit": 32.0}


def test_conversion_temperature_inferieure_au_zero_absolu():
    r = client.get("/celsius-fahrenheit", params={"celsius": -273.16})
    assert r.status_code == 400
    assert "zéro absolu" in r.json()["detail"]


def test_conversion_km_miles():
    r = client.get("/km-miles", params={"kilometres": 10})
    assert r.status_code == 200
    assert r.json() == {"kilometres": 10.0, "miles": 6.2137}


def test_conversion_km_miles_distance_negative():
    r = client.get("/km-miles", params={"kilometres": -5})
    assert r.status_code == 400
    assert "distance ne peut pas être négative" in r.json()["detail"]


def test_conversion_type_invalide():
    r = client.get("/celsius-fahrenheit", params={"celsius": "pas-un-nombre"})
    assert r.status_code == 422


def test_conversion_euros_devise():
    r = client.get("/euros-devise", params={"euros": 100, "devise": "USD"})
    assert r.status_code == 200
    assert r.json() == {
        "euros": 100.0,
        "devise": "USD",
        "montant_converti": 108.0,
    }


def test_conversion_euros_devise_montant_negatif():
    r = client.get("/euros-devise", params={"euros": -10, "devise": "USD"})
    assert r.status_code == 400
    assert "négatif" in r.json()["detail"]


def test_conversion_euros_devise_inconnue():
    r = client.get("/euros-devise", params={"euros": 50, "devise": "INCONNUE"})
    assert r.status_code == 400
    assert "Devise inconnue" in r.json()["detail"]