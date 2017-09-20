class Abilities:
    def __init__(self):
        self._attr = {
            'str': 0,
            'dex': 0,
            'con': 0,
            'cha': 0,
            'int': 0,
            'wis': 0
        }

    def get_ability(self, ability):
        try:
            return self._attr[ability.lower()]
        except KeyError:
            print('[ERR] Invalid ability!')

    def get_all_ability(self):
        return self._attr

    def set_ability(self, ability, rank):
        try:
            if not isinstance(rank, int):
                raise TypeError('[ERR] Invalid value for rank!')

            self._attr[ability.lower()] = rank
        except KeyError:
            print('[ERR] Invalid ability!')

    def incr_ability(self, ability, num = 1):
        try:
            self._attr[ability.lower()] += num
        except KeyError:
            print('[ERR] Invalid ability!')
