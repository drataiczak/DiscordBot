class Spellbook():
    def __init__(self):
        self._spellbook = []

    def add_spell(self, spell):
        if spell in self._spellbook:
            return True

        self._spellbook.append(spell)

    def get_spell(self, spell):
        index = self._spellbook.index(spell)
        return self._spellbook[index]

    def remove_spell(self, spell):
        self._spellbook.remove(spell)

    def get_spellbook(self):
        return self._spellbook
