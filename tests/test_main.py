"""Tests d'intégration des routes de l'API."""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_racine():
    reponse = client.get("/")
    assert reponse.status_code == 200
    assert reponse.json() == {"message": "Bienvenue sur l'API"}


def test_sante():
    reponse = client.get("/sante")
    assert reponse.status_code == 200
    assert reponse.json() == {"statut": "ok"}


def test_route_factorielle_succes():
    reponse = client.get("/math/factorielle?n=5")
    assert reponse.status_code == 200
    assert reponse.json() == {"n": 5, "resultat": 120}


def test_route_factorielle_erreur():
    reponse = client.get("/math/factorielle?n=-1")
    assert reponse.status_code == 400


def test_route_factorielle_invalide():
    reponse = client.get("/math/factorielle?n=abc")
    assert reponse.status_code == 422


def test_route_est_premier():
    reponse = client.get("/math/est-premier?n=7")
    assert reponse.status_code == 200
    assert reponse.json() == {"n": 7, "resultat": True}


def test_route_pgcd_succes():
    reponse = client.get("/math/pgcd?a=48&b=18")
    assert reponse.status_code == 200
    assert reponse.json() == {"a": 48, "b": 18, "resultat": 6}


def test_route_pgcd_invalide():
    reponse = client.get("/math/pgcd?a=abc&b=18")
    assert reponse.status_code == 422


def test_route_celsius_fahrenheit_succes():
    reponse = client.get("/celsius-fahrenheit?celsius=0")
    assert reponse.status_code == 200
    assert reponse.json() == {"celsius": 0.0, "fahrenheit": 32.0}


def test_route_celsius_fahrenheit_erreur():
    reponse = client.get("/celsius-fahrenheit?celsius=-300")
    assert reponse.status_code == 400


def test_route_celsius_fahrenheit_invalide():
    reponse = client.get("/celsius-fahrenheit?celsius=abc")
    assert reponse.status_code == 422