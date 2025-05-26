class Weather:
    def set_temperature(self, temperature):
        self.temperature = temperature

    def get_weather(self):
        return ('Температура воздуха составляет '
                f'{self.temperature} градусов тепла')
