from fastapi import FastAPI, HTTPException

from app.outils.math import est_premier, factorielle, pgcd

app = FastAPI(title="Mini API")


@app.get("/sante/")
def route_sante():
    return {"statut": "ok"}


@app.get("/factorielle/{n}")
def route_factorielle(n: int):
    try:
        return {"n": n, "resultat": factorielle(n)}
    except ValueError as e:
        raise HTTPException(400, detail=str(e))


@app.get("/est_premier/{n}")
def route_est_premier(n: int):
    return {"n": n, "resultat": est_premier(n)}


@app.get("/pgcd/{a}/{b}")
def route_pgcd(a: int, b:int):
    try:
        return {"a": a, "b": b, "resultat": pgcd(a,b)}
    except ValueError as e:
        raise HTTPException(400, detail=str(e))