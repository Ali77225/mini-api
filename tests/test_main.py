from fastapi.testclient import TestClient

from app.erreurs import (
    DEPASSEMENT_DE_LIMITE_MATH,
    LIMITE_FACTORIELLE,
    NOMBRE_NEGATIF_MATH,
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


