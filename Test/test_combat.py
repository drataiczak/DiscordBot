import sys
sys.path.append('/home/devin/Documents/Python/DiscordBot')
import DnD.combat as combat

def test_setters(cmb_obj):
    # Set all scores and increment to 9
    for stat, value in cmb_obj.get_all_cmb_stat().items():
        cmb_obj.set_stat(stat, 5)
        cmb_obj.incr_stat(stat)
        cmb_obj.incr_stat(stat, 3)

def test_getters(cmb_obj):
    for stat, value in cmb_obj.get_all_cmb_stat().items():
        if cmb_obj.get_cmb_stat(stat) != 9:
            return False

    return True

def combat_main():
    cmb_scores = combat.Combat()
    test_setters(cmb_scores)

    if not test_getters(cmb_scores):
        print('[!] test_getters() failed!')
        return False

    return True
