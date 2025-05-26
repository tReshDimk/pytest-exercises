class Cart:

    def __init__(self):
        self.items = []

    def add_item(self, item_name: str):
        self.items.append(item_name)

    def remove_item(self, item_name: str):
        if item_name in self.items:
            self.items.pop(self.items.index(item_name))
