from source.person import Person


def test_is_adult_when_age_is_more_18_true():
    test_person = Person(age=19)
    assert test_person.is_adult()
