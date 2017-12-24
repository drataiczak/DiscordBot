class Ability():
    def __str__(self):
        return ''.join('{}: {}; '.format(key, value) for key, value in self._ability.items())

    def __init__(self, name, isTrained, rank = 0):
        self._ability = {
            'name': name,
            'isTrained': isTrained,
            'rank': rank
        }

    def change_trained(self, value = True:
        self._ability['isTrained'] = value
