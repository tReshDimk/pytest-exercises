def test_str_equal():
    assert '123' == "123"


def test_one_is_true():
    assert 1


def test_tuple_equal_array():
    assert (2, 4, 5) == [2, 4, 5]


def test_sorted_tuple_equal_array():
    t1 = (5, 6, 3)
    assert [3, 5, 6] == sorted(t1)


def test_tuple_equal_sorted_tuple():
    t1 = (5, 6, 3)
    assert (3, 5, 6) == sorted(t1)
