from numb3rs import validate

def test_validate_chars():
    assert validate('cat') == False
    assert validate('a.b.b.c') == False

def test_validate_numbers():
    assert validate('0.0.0.0') == True
    assert validate("255.255.255.255") == True
    assert validate('275.275.275.275') == False
    assert validate("199.911.288.882") == False

if __name__ == "__main__":
    main()

