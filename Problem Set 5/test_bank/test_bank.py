from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello, Newman") == 0

def test_20():
    assert value("hola") == 20
    assert value("How") == 20

def test_100():
    assert value("What's") == 100
    assert value("") == 100

if __name__ == "__main__":
    main()
