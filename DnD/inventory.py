class Inventory:
    def __init__(self):
        self._weight = 0
        self._inv = []

    def add_item(self, item):
        self._inv.append(item)

    def remove_item(self, item):
        self._inv.remove(item)

    def get_items(self):
        return self._inv
