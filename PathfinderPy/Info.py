class Info():
    def __init__(self):
        self._info = {
            'player': None,
            'character': None,
            'alignment': None,
            'deity': None,
            'homeland': None,
            'race': None,
            'size': None,
            'gender': None,
            'age': 0,
            'height': (0, 0),
            'weight': 0,
            'hair': None,
            'eyes': None,
            'foot_spd': 0,
            'fly_spd': 0,
            'climb_spd': 0,
            'swim_spd': 0,
            'burrow_spd': 0
        }

    def set_info(self, pc, value, subpc = None):
        if pc == 'speed':
            if subpc == None:
                return False

            self._info[pc][subpc] = value

        self._info[pc] = value
        return True

    def get_info(self, pc, subpc = None):
        if pc == 'speed':
            if subpc == None:
                return None

            return self._info[pc][subpc]

        return self._info[pc]

    def get_all_info(self):
        return self._info
