class Inventory():
    def __init__(self):
        self._inventory = []

    def add_item(self, item):
        self._inventory.append(item)

    def get_item(self, item):
        indices = [i for index, obj in enumerate(self._inventory) if obj == item]

        if len(indices) <= 0:
            return None
        else:
            item_list = []

            for index in indices:
                item_list.append(indices[index])
                return item_list

    def get_all_items(self):
        return self._inventory
