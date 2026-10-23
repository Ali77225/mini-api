"""Point d'entrée de l'API FastAPI."""

"""Point d'entrée de l'API FastAPI."""

from fastapi import FastAPI, HTTPException

from app.outils.conversion import celsius_fahrenheit, km_mile
from app.outils.math import est_premier, factorielle, pgcd

app = FastAPI(title="Mini API")


@app.get("/")
def route_racine():
    return {"message": "Bienvenue sur l'API"}


@app.get("/sante/")
def route_sante():
    return {"statut": "ok"}


# --- Routes d'Ali (intactes) ---
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


# --- Ma route de conversion Celsius ---
@app.get("/celsius-fahrenheit")
def route_celsius_fahrenheit(celsius: float):
    try:
        return {"celsius": celsius, "fahrenheit": celsius_fahrenheit(celsius)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/km-mile")
def route_km_mile(km: float):
    try:
        return {"km": km, "miles": km_mile(km)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
