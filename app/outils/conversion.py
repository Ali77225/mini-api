from app.erreurs import ZERO_ABSOLU_CELSIUS, ConversionErreur


def celsius_fahrenheit(celsius: float) -> float:
    if celsius < ZERO_ABSOLU_CELSIUS:
        raise ConversionErreur(
            f"La température ne peut pas être inférieure au zéro absolu ({ZERO_ABSOLU_CELSIUS}°C)."
        )
    return round((celsius * 9 / 5) + 32, 2)