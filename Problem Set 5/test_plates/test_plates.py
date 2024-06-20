from plates import is_valid

# All vanity plates must start with at least two letters
def test_firsttwoletters():
    assert is_valid("CS") == True
    assert is_valid("50") == False
    assert is_valid("C5") == False
    assert is_valid("5S") == False
    assert is_valid("cs") == True

# Vanity plates may contain a max of 6 chars (letters or numbers) and a min of 2 chars.
def test_platelength():
    assert is_valid("C") == False
    assert is_valid("CS") == True
    assert is_valid("HELLOCS50") == False
    assert is_valid("CS50") == True

# Numbers cannot be used in the middle of a plate and the first number used cannot be a ‘0’.
def test_validatenumbers():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("CSP001") == False
    assert is_valid("CSP5AA") == False

# No periods, spaces, or punctuation marks are allowed.
def test_specialchars():
    assert is_valid("PI3.14") == False
    assert is_valid("How,RU") == False
    assert is_valid("W H O") == False
