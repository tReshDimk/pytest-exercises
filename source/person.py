# класс описывает человека
class Person():
    def __init__(self, age: int):
        self.age = age

    # метод, который проверяет возраст
    def is_adult(self):
        # установим возраст совершеннолетия
        adult_age = 18
        # вернём результат сравнения аргумента age с возрастом совершеннолетия
        return self.age >= adult_age
