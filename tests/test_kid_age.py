from pytest import approx

from source.kid_age import kid_age


def test_kid_age_when_age_is_5dot5():
    assert 5.5 == approx(kid_age(5, 5, 15), 0.01)
