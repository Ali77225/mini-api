from fastapi import FastAPI, HTTPException

from app.outils.math import factorielle

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