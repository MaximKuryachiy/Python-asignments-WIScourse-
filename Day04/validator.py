def convert(player_choice):
    try:
        conv_player_choice = int(player_choice)
    except ValueError:
        print('Please, enter a valid value (a number between 1 and 20 or x, n, s commands)')
        return False
    return conv_player_choice