from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.erreurs import MetierException
from app.outils.conversion import celsius_fahrenheit

app = FastAPI(title="Mini API")


@app.exception_handler(MetierException)
async def gerer_erreur_metier(request: Request, exc: MetierException) -> JSONResponse:
    return JSONResponse(status_code=400, content={"detail": str(exc)})


@app.get("/sante")
def sante():
    return {"statut": "ok"}


@app.get("/celsius-fahrenheit")
def route_celsius_fahrenheit(celsius: float):
    resultat = celsius_fahrenheit(celsius)
    return {"celsius": celsius, "fahrenheit": resultat}