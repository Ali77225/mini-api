from app.outils.texte import est_palindrome


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