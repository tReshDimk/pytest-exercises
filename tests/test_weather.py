import pytest

from source.weather import Weather


class TestWeather:

    @pytest.fixture(autouse=True)
    def weather(self):
        self.forecast = Weather()
        self.forecast.set_temperature(25)
        return self.forecast

    def test_weather_return_text(self):
        assert self.forecast.get_weather() == 'Температура воздуха составляет 25 градусов тепла'

    def test_weather_change_return_new_text(self):
        self.forecast.set_temperature(10)
        assert self.forecast.get_weather() == 'Температура воздуха составляет 10 градусов тепла'
