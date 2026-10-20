from fastapi import FastAPI, HTTPException
from app.outils.conversion import celsius_fahrenheit
from app.erreurs import ConversionErreur

app = FastAPI(title="Mini API")


@app.get("/sante")
def sante():
    return {"statut": "ok"}


@app.get("/celsius-fahrenheit")
def route_celsius_fahrenheit(celsius: float):
    try:
        resultat = celsius_fahrenheit(celsius)
        return {"celsius": celsius, "fahrenheit": resultat}
    except ConversionErreur as e:
        raise HTTPException(status_code=400, detail=str(e))