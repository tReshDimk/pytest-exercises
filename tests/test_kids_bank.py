import pytest

from source.kids_bank import KidsBank


class TestKidsBank:
    # init tests
    def test_init_valid_data(self):
        bank = KidsBank(10, {'Foo', 'Woo'})
        assert bank.amount == 10
        assert bank.friends_set == {'Foo', 'Woo'}

    def test_init_when_friends_is_none_empty_set(self):
        bank = KidsBank(100, None)
        assert type(bank.friends_set) is set
        assert len(bank.friends_set) == 0

    def test_init_friends_set_value_error(self):
        with pytest.raises(TypeError):
            KidsBank(50, ['Ben', 'John'])

    def test_init_when_amount_is_less_then_1_value_error(self):
        with pytest.raises(ValueError):
            KidsBank(0)

    # other tests
    def test_add_friend(self):
        bank = KidsBank(9, {'Sam', 'Jack'})
        bank.add_friend('Tom')
        assert bank.friends_set == {'Sam', 'Jack', 'Tom'}

    def test_add_money(self):
        bank = KidsBank(15)
        bank.add_money(5)
        assert bank.amount == 20

    def test_divide_money(self):
        bank = KidsBank(100, {'Ben', 'Tom', 'Chack'})
        assert [33.3, 33.3, 33.3] == pytest.approx(bank.divide_money(), 0.01)
