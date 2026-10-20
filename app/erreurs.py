"""Erreurs communes de l'API"""


class MetierException(Exception):
    pass


class ConversionErreur(MetierException):
    pass


ZERO_ABSOLU_CELSIUS = -273.15