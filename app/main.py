"""Point d'entrée de l'API FastAPI."""

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

from app.erreurs import MetierException
from app.outils.conversion import celsius_fahrenheit, km_mile
from app.outils.math import est_premier, factorielle, pgcd
from app.outils.texte import compter_voyelles, est_palindrome

app = FastAPI(title="Mini-API")


@app.exception_handler(MetierException)
def metier_exception_handler(_request: Request, exc: MetierException):
    return JSONResponse(status_code=400, content={"message": str(exc)})


@app.get("/")
def route_racine():
    return {"message": "Bienvenue sur l'API"}


@app.get("/sante/")
def route_sante():
    return {"statut": "ok"}


@app.get("/factorielle/{n}")
def route_factorielle(n: int):
    try:
        return {"n": n, "resultat": factorielle(n)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/est_premier/{n}")
def route_est_premier(n: int):
    return {"n": n, "resultat": est_premier(n)}


@app.get("/pgcd/{a}/{b}")
def route_pgcd(a: int, b: int):
    try:
        return {"a": a, "b": b, "resultat": pgcd(a, b)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/celsius-fahrenheit")
def route_celsius_fahrenheit(celsius: float):
    return {"celsius": celsius, "fahrenheit": celsius_fahrenheit(celsius)}


@app.get("/km-mile")
def route_km_mile(km: float):
    return {"km": km, "miles": km_mile(km)}


@app.get("/est_palindrome")
def route_est_palindrome(texte: str):
    return {"texte": texte, "resultat": est_palindrome(texte)}


@app.get("/compter_voyelles")
def route_compter_voyelles(texte: str):
    return {"texte": texte, "resultat": compter_voyelles(texte)}