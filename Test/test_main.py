import test_ability as ability
import test_combat as combat

def main():
    total = 0
    failed = 0

    total += 1
    if not ability.ability_main():
        failed += 1

    total += 1
    if not combat.combat_main():
        failed += 1
        
    exit_stat(failed, total)

def exit_stat(failed, total):
    print('[+] Tests succeeded: %d/%d' % (total - failed, total))
    print('[!] Tests failed: %d' % failed)
