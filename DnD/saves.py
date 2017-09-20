class Saves:
    def __init__(self):
        self._saves = {
            'fortitude': 0,
            'reflex': 0,
            'will': 0
        }

    def set_save(self, save, rank):
        self._saves[save] = rank

    def get_save(self, save):
        return self._saves[save]

    def get_all_saves(self):
        return self._saves

    def incr_save(self, save, rank = 1):
        self._save += rank
