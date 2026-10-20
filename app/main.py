from fastapi import HTTPException
from app.outils.conversion import celsius_fahrenheit
from app.erreurs import ConversionErreur

@app.get("/celsius-fahrenheit")
def route_celsius_fahrenheit(celsius: float):
    try:
        resultat = celsius_fahrenheit(celsius)
        return {"celsius": celsius, "fahrenheit": resultat}
    except ConversionErreur as e:
        raise HTTPException(status_code=400, detail=str(e))