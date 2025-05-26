import pytest

from source.multiply import multiply


@pytest.mark.parametrize(
        'a, b, expected',
        [
            [1, 2, 2],
            [3, 3, 9],
            [-2, 3, -6],
            [0, 10, 0]
        ]
    )
def test_multiply(a, b, expected):
    # ваш код здесь
    assert multiply(a, b) == expected
