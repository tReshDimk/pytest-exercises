class KidsBank:

    def __init__(self, amount: int, friends_set=None):
        if friends_set is None:
            friends_set = set()
        if type(friends_set) is not set:
            raise TypeError
        if amount < 1:
            raise ValueError
        else:
            self.friends_set = friends_set
            self.amount = amount

    def add_friend(self, name: str):
        self.friends_set.add(name)

    def add_money(self, sum: int):
        self.amount += sum

    def divide_money(self):
        res = (
                [round(self.amount / len(self.friends_set), 2)]
                * (len(self.friends_set) - 1)
            )
        res.append(round(self.amount - sum(res), 2))
        return res


if __name__ == '__main__':
    bank = KidsBank(100, {'Ben', 'Tom', 'Chack'})
    print(bank.divide_money())
