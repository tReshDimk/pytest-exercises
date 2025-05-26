from source.max_number import get_max_number_from_list


def test_get_max_number_from_list_correct_list():
    arg = [0, 1, 2, 3, 4, -5, 6.5]
    assert get_max_number_from_list(arg) == 6.5


def test_get_max_number_from_list_not_list_error():
    arg = 'String'
    assert get_max_number_from_list(arg) == 'Not list!'


def test_get_max_number_from_list_empty_list_error():
    assert get_max_number_from_list([]) == 'List is empty!'


def test_get_max_number_from_list_incorrect_type_element_error():
    assert get_max_number_from_list(['abc', 34]) == 'List contains a not number type element!'

