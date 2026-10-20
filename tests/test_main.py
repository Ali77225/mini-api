from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_sante():
    r = client.get("/sante")
    assert r.status_code == 200
    assert r.json() == {"statut": "ok"}


def test_conversion_celsius_fahrenheit():
    r = client.get("/celsius-fahrenheit", params={"celsius": 0})
    assert r.status_code == 200
    assert r.json() == {"celsius": 0.0, "fahrenheit": 32.0}


def test_conversion_temperature_inferieure_au_zero_absolu():
    r = client.get("/celsius-fahrenheit", params={"celsius": -300})
    assert r.status_code == 400
    assert "zéro absolu" in r.json()["detail"]