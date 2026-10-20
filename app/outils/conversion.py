from app.erreurs import ZERO_ABSOLU_CELSIUS, ConversionErreur


def km_miles(kilometres: float) -> float:
    if kilometres < 0:
        raise ConversionErreur("La distance ne peut pas être négative.")
    return round(kilometres * 0.62137, 4)


def celsius_fahrenheit(celsius: float) -> float:
    if celsius < ZERO_ABSOLU_CELSIUS:
        raise ConversionErreur(
            f"La température ne peut pas être inférieure au zéro absolu ({ZERO_ABSOLU_CELSIUS}°C)."
        )
    return round((celsius * 9 / 5) + 32, 2)