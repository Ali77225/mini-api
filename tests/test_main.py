from fastapi.testclient import TestClient

from app.erreurs import (
    DEPASSEMENT_DE_LIMITE_MATH,
    DEVISE_NON_SUPPORTEE_FINANCE,
    LIMITE_FACTORIELLE,
    MONTANT_NEGATIF_FINANCE,
    NOMBRE_NEGATIF_MATH,
    PGCD_INDEFINI_MATH,
)
from app.main import app

client = TestClient(app)


def test_sante():
    r = client.get("/sante")
    assert r.status_code == 200
    assert r.json() == {"statut": "ok"}


# Tests de la route factorielle
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


# Tests de la route est_premier
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


# Tests de la route pgcd
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


# Tests de la route celsius_fahrenheit
def test_route_celsius_fahrenheit_succes():
    r = client.get("/celsius-fahrenheit?celsius=0")
    assert r.status_code == 200
    assert r.json() == {"celsius": 0.0, "fahrenheit": 32.0}


def test_route_celsius_fahrenheit_erreur():
    r = client.get("/celsius-fahrenheit?celsius=-300")
    assert r.status_code == 400


def test_route_celsius_fahrenheit_mauvais_type():
    r = client.get("/celsius-fahrenheit?celsius=abc")
    assert r.status_code == 422


# Tests de la route km-mile
def test_route_km_mile_succes():
    r = client.get("/km-mile?km=10")
    assert r.status_code == 200
    assert r.json() == {"km": 10.0, "miles": 6.21}


def test_route_km_mile_erreur():
    r = client.get("/km-mile?km=-5")
    assert r.status_code == 400


def test_route_km_mile_mauvais_type():
    r = client.get("/km-mile?km=abc")
    assert r.status_code == 422


# Tests de la route est_palindrome
def test_route_est_palindrome_vrai():
    r = client.get("/est_palindrome", params={"texte": "Ésope reste ici et se repose"})
    assert r.status_code == 200
    assert r.json() == {"texte": "Ésope reste ici et se repose", "resultat": True}


def test_route_est_palindrome_faux():
    r = client.get("/est_palindrome", params={"texte": "bonjour"})
    assert r.status_code == 200
    assert r.json() == {"texte": "bonjour", "resultat": False}


def test_route_est_palindrome_texte_vide():
    r = client.get("/est_palindrome", params={"texte": ""})
    assert r.status_code == 200
    assert r.json()["resultat"] is True


def test_route_est_palindrome_texte_absent():
    r = client.get("/est_palindrome")
    assert r.status_code == 422


# Tests de la route compter_voyelles
def test_route_compter_voyelles():
    r = client.get("/compter_voyelles", params={"texte": "Bonjour le monde"})
    assert r.status_code == 200
    assert r.json() == {"texte": "Bonjour le monde", "resultat": 6}


def test_route_compter_voyelles_texte_vide():
    r = client.get("/compter_voyelles", params={"texte": ""})
    assert r.status_code == 200
    assert r.json()["resultat"] == 0


def test_route_compter_voyelles_texte_absent():
    r = client.get("/compter_voyelles")
    assert r.status_code == 422


# Tests de la route inverser
def test_route_inverser():
    r = client.get("/inverser", params={"texte": "Bonjour le monde"})
    assert r.status_code == 200
    assert r.json() == {"texte": "Bonjour le monde", "resultat": "ednom el ruojnoB"}


def test_route_inverser_texte_vide():
    r = client.get("/inverser", params={"texte": ""})
    assert r.status_code == 200
    assert r.json()["resultat"] == ""


def test_route_inverser_texte_absent():
    r = client.get("/inverser")
    assert r.status_code == 422


def test_route_euro_devise_succes():
    response = client.get("/euro-devise?montant=100&devise=USD")
    assert response.status_code == 200
    assert response.json() == {"montant": 100.0, "devise": "USD", "resultat": 108.0}


def test_route_euro_devise_zero():
    response = client.get("/euro-devise?montant=0&devise=USD")
    assert response.status_code == 200
    assert response.json() == {"montant": 0.0, "devise": "USD", "resultat": 0.0}


def test_route_euro_devise_montant_negatif():
    response = client.get("/euro-devise?montant=-10&devise=USD")
    assert response.status_code == 400
    assert response.json()["detail"] == MONTANT_NEGATIF_FINANCE


def test_route_euro_devise_inconnue():
    response = client.get("/euro-devise?montant=100&devise=XYZ")
    assert response.status_code == 400
    assert response.json()["detail"] == DEVISE_NON_SUPPORTEE_FINANCE


def test_route_euro_devise_type_invalide():
    response = client.get("/euro-devise?montant=abc&devise=USD")
    assert response.status_code == 422
