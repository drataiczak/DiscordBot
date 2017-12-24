import PathfinderPy as pf
import Character as char

def basic_info():
    info_list = char.char_info.get_all_info().items()
    in_list = []

    # We could iterate through all Info items but this would cause weird printables
    print('[I] Press enter for items you do not wish to use.\n')

    in_list.append(input('[+] Your name: '))
    in_list.append(input('[+] Character name: '))
    in_list.append(input('[+] Race: '))
    in_list.append(input('[+] Gender: '))
    in_list.append(input('[+] Age: '))
    in_list.append(input('[+] Alignment: '))
    in_list.append(input('[+] Deity: '))
    in_list.append(input('[+] Homeland: '))
    in_list.append(input('[+] Size: '))
    in_list.append(input('[+] Height (ft): '))
    in_list.append(input('[+] Height (in): '))
    in_list.append(input('[+] Weight: '))
    in_list.append(input('[+] Hair: '))
    in_list.append(input('[+] Eyes: '))
    in_list.append(input('[+] Ground speed (ft): '))
    in_list.append(input('[+] Fly speed (ft): '))
    in_list.append(input('[+] Climb speed (ft): '))
    in_list.append(input('[+] Swim speed (ft): '))
    in_list.append(input('[+] Burrow speed (ft): '))

    in_iter = iter(in_list)

    for key, value in info_list:
        char.char_info.set_info(key, next(in_iter))

def main():
    print('[I] This program will now guide you through creation of a Pathfinder character.')

    basic_info()
