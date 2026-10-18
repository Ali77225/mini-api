from app.erreurs import ConversionErreur


def celsius_fahrenheit(celsius: float) -> float:
    if celsius < -273.15:
        raise ConversionErreur("La température ne peut pas être inférieure au zéro absolu (-273.15°C).")
    return round((celsius * 9 / 5) + 32, 2)