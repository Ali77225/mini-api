from app.outils.texte import compter_voyelles, est_palindrome, inverser


def test_est_palindrome_mot():
    assert est_palindrome("kayak") is True


def test_est_palindrome_mot_non_palindrome():
    assert est_palindrome("bonjour") is False


def test_est_palindrome_phrase():
    assert est_palindrome("Ésope reste ici et se repose") is True


def test_est_palindrome_phrase_non_palindrome():
    assert est_palindrome("Thomas joue au foot") is False


def test_est_palindrome_une_lettre():
    assert est_palindrome("a") is True


def test_est_palindrome_chiffres():
    assert est_palindrome("2002") is True


def test_est_palindrome_chiffres_et_ponctuation():
    assert est_palindrome("1,1") is True


def test_est_palindrome_texte_vide():
    assert est_palindrome("") is True


def test_est_palindrome_que_de_la_ponctuation():
    assert est_palindrome("???") is True




def test_compter_voyelles_mot():
    assert compter_voyelles("bonjour") == 3


def test_compter_voyelles_avec_y():
    assert compter_voyelles("Python") == 2


def test_compter_voyelles_accents():
    assert compter_voyelles("Élève") == 3


def test_compter_voyelles_phrase():
    assert compter_voyelles("Bonjour le monde") == 6


# compter_voyelles : cas limites
def test_compter_voyelles_texte_vide():
    assert compter_voyelles("") == 0


def test_compter_voyelles_sans_voyelle():
    assert compter_voyelles("bcdfg") == 0


def test_compter_voyelles_majuscules():
    assert compter_voyelles("AEIOUY") == 6


def test_compter_voyelles_chiffres_et_ponctuation():
    assert compter_voyelles("123 !?") == 0



# inverser : cas normaux
def test_inverser_mot():
    assert inverser("bonjour") == "ruojnob"


def test_inverser_phrase():
    assert inverser("Bonjour le monde") == "ednom el ruojnoB"


def test_inverser_accents_et_majuscules():
    assert inverser("Été") == "étÉ"


# inverser : cas limites
def test_inverser_texte_vide():
    assert inverser("") == ""


def test_inverser_une_lettre():
    assert inverser("a") == "a"


def test_inverser_palindrome():
    assert inverser("kayak") == "kayak"


def test_inverser_chiffres_et_ponctuation():
    assert inverser("123 !?") == "?! 321"