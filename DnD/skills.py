class Skills:
    def __init__(self):
        self._skills = {
            'acrobatics': 0,
            'appraise': 0,
            'bluff': 0,
            'climb': 0,
            'craft': 0,
            'diplomacy': 0,
            'disable_device': 0,
            'disguise': 0,
            'escape_artist': 0,
            'fly': 0,
            'handle_animal': 0,
            'heal': 0,
            'intimidate': 0,
            'knowledge': {
                'arcana': 0,
                'dungeoneering': 0,
                'engineering': 0,
                'geography': 0,
                'history': 0,
                'local': 0,
                'nature': 0,
                'nobility': 0,
                'planes': 0,
                'religion': 0
            },
            'linguistics': 0,
            'perception': 0,
            'perform': 0,
            'profession': 0,
            'ride': 0,
            'sense_motive': 0,
            'sleight_of_hand': 0,
            'spellcraft': 0,
            'stealth': 0,
            'survival': 0,
            'swim': 0,
            'magic_device': 0
        }

    def set_skill(self, skill, subskill = None, rank):
        if skill == 'knowledge':
            if subskill == None:
                print('[ERR] Please choose a subskill')
                return False

            self._skills[skill][subskill] = rank
        self._skills[skill] = rank

    def set_trained(self, skill, subskill = None):
        if skill == 'knowledge':
            if subskill == None:
                print('[ERR] Please choose a subskill')
                return False

            self._skills[skill][subskill] += 3
        self._skills[skill] += 3

    def get_skill(self, skill, subskill = None):
        if skill == 'knowledge':
            if subskill == None:
                print('[ERR] Please choose a subskill')
                return None

            return self._skills[skill][subskill]
        return self._skills[skill]

    def incr_skill(self, skill, subskill = None, rank = 1):
        if skill == 'knowledge':
            if subskill == None:
                print('[ERR] Please choose a subskill')
                return None

            self._skills[skill][subskill] += rank
        self._skills[skill] += rank
