import unicodedata


def est_palindrome(texte: str) -> bool:
    minuscules = texte.lower()
    decompose = unicodedata.normalize("NFD", minuscules)
    nettoye = ""
    for caractere in decompose:
        if caractere.isalnum():
            nettoye += caractere
    return nettoye == nettoye[::-1]




def compter_voyelles(texte: str) -> int:
    minuscules = texte.lower()
    decompose = unicodedata.normalize("NFD", minuscules)
    nombre = 0
    for caractere in decompose:
        if caractere in "aeiouy":
            nombre += 1
    return nombre





def inverser(texte: str) -> str:
    return texte[::-1]