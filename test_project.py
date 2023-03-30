from project import validate_mobile, validate_stud_email, validate_password


def test_validate_mobile():
    assert validate_mobile("+27") == False
    assert validate_mobile("+27812799063") == True


def test_validate_stud_email():
    assert validate_stud_email("ethan@") == False
    assert validate_stud_email("diedericksethan@@gmail.com") == False
    assert validate_stud_email("diedericks.ethan@gmail.com") == True


def test_validate_password():
    assert validate_password("Ethan1") == False
    assert validate_password("dsadhiasdwd2*") == False
    assert validate_password("Strongpassword1j*") == True
