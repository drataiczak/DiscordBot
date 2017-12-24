class Spell():
    def __str__(self):
        return ''.join('{}: {}; '.format(key, value) for key, value in self._spell.items())

    def __init__(self, name, description, level):
        self._spell = {
            'name': name,
            'description': description,
            'level': level
        }
