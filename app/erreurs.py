"""Erreurs communes de l'API."""


class ConversionErreur(ValueError):
    """Erreur levée lors d'une conversion invalide."""


ZERO_ABSOLU_CELSIUS = -273.15

# Module math
NOMBRE_NEGATIF_MATH = "Entrée négative, veuillez entrer un nombre positif"
LIMITE_FACTORIELLE = 800
DEPASSEMENT_DE_LIMITE_MATH = f"Limite dépassée, veuillez entrer un nombre <= {LIMITE_FACTORIELLE}"
PGCD_INDEFINI_MATH = "Le pgcd(0,0) n'existe pas"
