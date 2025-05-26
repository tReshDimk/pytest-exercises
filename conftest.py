import pytest

from source.mail import Mail
from source.cart import Cart
from source.movie_collection import MovieCollection


@pytest.fixture
def mail():
    return Mail('holmes@yandex.ru', 'watson@yandex.ru')


@pytest.fixture
def cart():
    test_cart = Cart()
    for i in ['апельсиновый сок', 'манго', 'молоко']:
        test_cart.add_item(i)
    return test_cart


@pytest.fixture(scope='session')
def city_name():
    return []


@pytest.fixture(scope='session')
def append_city(city_name):
    city_name.append('Moscow')


@pytest.fixture
def movie_collection():

    movies = [
        ('The Green Mile', 1999, 9.1),
        ('The Shawshank Redemption', 1994, 9.17),
        ('1+1', 2011, 8.8),
        ('Flight Club', 1999, 8.6),
    ]

    collection = MovieCollection()

    for movie in movies:
        collection.add_movie(*movie)

    return collection
