"""Module de centralisation des erreurs et constantes."""

"""Exceptions personnalisées de l'API."""


class MetierException(Exception):
    """Exception de base pour les erreurs métier."""


class MathErreur(MetierException):
    """Erreur levée lors d'un calcul mathématique invalide."""


class ConversionErreur(MetierException):
    """Erreur levée lors d'une conversion invalide."""


ZERO_ABSOLU_CELSIUS = -273.15

# Module math
NOMBRE_NEGATIF_MATH = "Entrée négative, veuillez entrer un nombre positif"
LIMITE_FACTORIELLE = 800
DEPASSEMENT_DE_LIMITE_MATH = (
    f"Limite dépassée, veuillez entrer un nombre <= {LIMITE_FACTORIELLE}"
)
PGCD_INDEFINI_MATH = "Le pgcd(0,0) n'existe pas"


MONTANT_NEGATIF_FINANCE = "Le montant ne peut pas être négatif"
DEVISE_NON_SUPPORTEE_FINANCE = "Devise non supportée"
