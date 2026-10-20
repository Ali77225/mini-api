from fastapi.testclient import TestClient

from app.erreurs import (
    DEPASSEMENT_DE_LIMITE_MATH,
    LIMITE_FACTORIELLE,
    NOMBRE_NEGATIF_MATH,
    PGCD_INDEFINI_MATH,
)
from app.main import app

client = TestClient(app)
def test_sante():
    r = client.get("/sante")
    assert r.status_code == 200
    assert r.json() == {"statut": "ok"}

def test_route_factorielle_de_5():
    r = client.get(f"/factorielle/{5}")
    assert r.status_code == 200
    assert r.json()["resultat"] == 120

def test_route_factorielle_hors_limite():
    r = client.get(f"/factorielle/{LIMITE_FACTORIELLE + 1}")
    assert r.status_code == 400
    assert r.json()["detail"] == DEPASSEMENT_DE_LIMITE_MATH

def test_route_factorielle_negatif():
    r = client.get("/factorielle/-1")
    assert r.status_code == 400
    assert r.json()["detail"] == NOMBRE_NEGATIF_MATH

def test_route_factorielle_mauvais_type():
    r = client.get("/factorielle/abc")
    assert r.status_code == 422


def test_route_est_premier_de_3():
    r = client.get("/est_premier/3")
    assert r.status_code == 200
    assert r.json()["resultat"] is True

def test_route_est_premier_de_8():
    r = client.get("/est_premier/8")
    assert r.status_code == 200
    assert r.json()["resultat"] is False

def test_route_est_premier_nombre_negatif():
    r = client.get("/est_premier/-3")
    assert r.status_code == 200
    assert r.json()["resultat"] is False

def test_route_est_premier_mauvais_type():
    r = client.get("/est_premier/abc")
    assert r.status_code == 422


def test_route_pgcd_normal():
    r = client.get("/pgcd/22/16")
    assert r.status_code == 200
    assert r.json()["resultat"] == 2

def test_route_pgcd_negatif():
    r = client.get("/pgcd/-22/16")
    assert r.status_code == 200
    assert r.json()["resultat"] == 2

def test_route_pgcd_b_nul():
    r = client.get("/pgcd/7/0")
    assert r.status_code == 200
    assert r.json()["resultat"] == 7

def test_route_pgcd_indéfinis():
    r = client.get("/pgcd/0/0")
    assert r.status_code == 400
    assert r.json()["detail"] == PGCD_INDEFINI_MATH

def test_route_pgcd_mauvais_type():
    r = client.get("/pgcd/abc/16")
    assert r.status_code == 422
