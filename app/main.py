"""Point d'entrée de l'API FastAPI."""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.erreurs import MetierException
from app.outils import math
from app.outils.conversion import celsius_fahrenheit

app = FastAPI(title="Mini-API")


@app.exception_handler(MetierException)
@app.exception_handler(ValueError)
def metier_exception_handler(_request: Request, exc: MetierException):
    return JSONResponse(status_code=400, content={"message": str(exc)})


@app.get("/")
def route_racine():
    return {"message": "Bienvenue sur l'API"}


@app.get("/sante")
def route_sante():
    return {"statut": "ok"}


@app.get("/math/factorielle")
def route_factorielle(n: int):
    return {"n": n, "resultat": math.factorielle(n)}


@app.get("/math/est-premier")
def route_est_premier(n: int):
    return {"n": n, "resultat": math.est_premier(n)}


@app.get("/math/pgcd")
def route_pgcd(a: int, b: int):
    return {"a": a, "b": b, "resultat": math.pgcd(a, b)}


@app.get("/celsius-fahrenheit")
def route_celsius_fahrenheit(celsius: float):
    return {"celsius": celsius, "fahrenheit": celsius_fahrenheit(celsius)}