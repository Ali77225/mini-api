"""Erreurs communes de l'API"""


class MetierException(Exception):
    pass


class ConversionErreur(ValueError, MetierException):
    pass


ZERO_ABSOLU_CELSIUS = -273.15