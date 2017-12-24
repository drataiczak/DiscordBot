import sys
sys.path.append('/home/devin/Documents/Python/DiscordBot')
import DnD.ability as ability

def test_setters(ability_obj):
    # Set all scores and increment to 9
    for ability, value in ability_obj.get_all_ability().items():
        ability_obj.set_ability(ability, 5)
        ability_obj.incr_ability(ability)
        ability_obj.incr_ability(ability, 3)

def test_getters(ability_obj):
    for ability, value in ability_obj.get_all_ability().items():
        if ability_obj.get_ability(ability) != 9:
            return False

    return True

def ability_main():
    scores = ability.Abilities()
    test_setters(scores)

    if not test_getters(scores):
        print('[!] test_getters() failed!')
        return False

    return True
