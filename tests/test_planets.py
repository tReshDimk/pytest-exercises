from source.planets import get_planet_by_number


def test_get_planet_by_number_when_planet_is_4_mars():
    assert get_planet_by_number(4) == "Mars"


def test_get_planet_by_number_when_number_is_more_then_8_value_error():
    assert get_planet_by_number(12) == "I don't know"
