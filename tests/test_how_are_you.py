from pytest import raises

from source.how_are_you import how_are_you, WrongSeasonException


def test_how_are_you_when_season_is_wrong():
    with raises(WrongSeasonException):
        how_are_you("Sunday")
