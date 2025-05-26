import pytest

from source.mail import Mail
from source.cart import Cart


@pytest.fixture
def mail():
    return Mail('holmes@yandex.ru', 'watson@yandex.ru')


@pytest.fixture
def cart():
    test_cart = Cart()
    for i in ['апельсиновый сок', 'манго', 'молоко']:
        test_cart.add_item(i)
    return test_cart
