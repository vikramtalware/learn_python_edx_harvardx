from twttr import shorten

def main():
    test_shorten_case()
    test_default()
    test_novowels()

def test_shorten_case():
    assert shorten("TwittEr") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"

def test_default():
    assert shorten("") == ""

def test_novowels():
    assert shorten("CS50") == "CS50"

if __name__ == "__main__":
    main()
