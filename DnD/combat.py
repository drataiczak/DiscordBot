class Combat:
    def __init__(self):
        self._cmb_stats = {
            'health': 0,
            'initiative': 0,
            'armor_class': 0,
            'touch_ac': 0,
            'ff_ac': 0,
            'base_atk_bonus': 0,
            'spell_resist': 0,
            'cmb': 0,
            'cmd': 0
        }

    def get_cmb_stat(self, stat):
        try:
            return self._cmb_stats[stat.lower()]
        except KeyError:
            print('[ERR] Invalid combat stat!')

    def get_all_cmb_stat(self):
        return self._cmb_stats

    def set_stat(self, stat, rank):
        try:
            if not isinstance(rank, int):
                raise TypeError('Invalid value for rank!')

            self._cmb_stats[stat.lower()] = rank
        except KeyError:
            print('[ERR] Invalid combat stat!')

    def incr_stat(self, stat, num = 1):
        try:
            self._cmb_stats[stat.lower()] += num
        except KeyError:
            print('[ERR] Invalid combat stat!')
