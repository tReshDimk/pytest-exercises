import pytest


def test_cart_remove_item(cart):
    cart.remove_item('манго')
    assert 'манго' not in cart.items


@pytest.mark.parametrize('item', ['апельсиновый сок', 'манго', 'молоко'])
def test_cart_item_in_product_list(cart, item):
    assert item in cart.items
