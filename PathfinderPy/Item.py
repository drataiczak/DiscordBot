class Item():
    def __str__(self):
        return ''.join('{}: {}; '.format(key, value) for key, value in self._item.items())

    def __init__(self, name, value, weight = 0, description = None):
        self._item = {
            'name': name,
            'description': description,
            'value': value,
            'weight': weight
        }
