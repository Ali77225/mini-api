"""MODULE de math avec les fonctions factorielle, est_premier et pgcd"""

from app.erreurs import (
    DEPASSEMENT_DE_LIMITE_MATH,
    LIMITE_FACTORIELLE,
    NOMBRE_NEGATIF_MATH,
)


def factorielle(n: int) -> int:
    if n < 0:
        raise ValueError(NOMBRE_NEGATIF_MATH)
    if n > LIMITE_FACTORIELLE:
        raise ValueError(DEPASSEMENT_DE_LIMITE_MATH)
    return 1 if n <= 1 else n * factorielle(n - 1) 


def est_premier(n: int) -> bool:
    if n <= 1 :
        return False
    d = 2
    while d * d <= n :
        if n % d == 0 :
            return False
        d += 1
    return True