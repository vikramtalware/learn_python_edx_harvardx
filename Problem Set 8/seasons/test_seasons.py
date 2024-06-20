from seasons import age_min
from datetime import date

def test_age_min():
    assert age_min(date(1999, 1, 1), date(2000, 1, 1)) == 525600
    assert age_min(date(2001, 1, 1), date(2003, 1, 1)) == 1051200
    assert age_min(date(1995, 1, 1), date(2000, 1, 1)) == 2629440
    assert age_min(date(2020, 6, 1), date(2032, 1, 1)) == 6092640
