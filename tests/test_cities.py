class TestClassCityName:
    def test_city_name_one_city_is_in_received_list(
                self, city_name, append_city
            ):
        assert city_name == ['Moscow']


class TestClassCityNameWithoutAppend:
    def test_city_name_one_city_is_in_received_list(self, city_name):
        assert city_name == ['Moscow']
