import unicodedata


def est_palindrome(texte: str) -> bool:
    minuscules = texte.lower()
    decompose = unicodedata.normalize("NFD", minuscules)
    nettoye = ""
    for caractere in decompose:
        if caractere.isalnum():
            nettoye += caractere
    return nettoye == nettoye[::-1]