from um import count

def test_count():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
    assert count("cat") == 0
    assert count("um") == 1
    assert count("Um?") == 1