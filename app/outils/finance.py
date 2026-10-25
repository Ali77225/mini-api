from app.erreurs import DEVISE_NON_SUPPORTEE_FINANCE, MONTANT_NEGATIF_FINANCE


class FinanceErreur(ValueError):
    """Exception levée pour les erreurs du module finance."""


TAUX_CONVERSION = {
    "USD": 1.08,
    "GBP": 0.85,
    "JPY": 165.0,
    "CHF": 0.95,
}


def euro_devise(montant: float, devise: str) -> float:
    """Convertit un montant en euros vers une autre devise."""
    if montant < 0:
        raise FinanceErreur(MONTANT_NEGATIF_FINANCE)

    devise_upper = devise.upper()
    if devise_upper not in TAUX_CONVERSION:
        raise FinanceErreur(DEVISE_NON_SUPPORTEE_FINANCE)

    return round(montant * TAUX_CONVERSION[devise_upper], 2)
