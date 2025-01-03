def main():

    import comparisator
    import validator
    import random

    print('Welcome to number guesser game!')
    count = 0
    computer_number = random.randrange(1, 20, 1)
    print('The computer generated a number!')
    while True:

        player_choice = input('Now player, enter a number (from 1 to 20):')
        if str(player_choice) == 'x':
            print('Goodbye!')
            break
        elif str(player_choice) == 'n':
            count = 0
            computer_number = random.randrange(1, 20, 1)
            continue
        elif str(player_choice) == 's':
            print(computer_number , 'Don`t cheat :(')
            count = 0
            computer_number = random.randrange(1, 20, 1)
            continue

        #print(player_choice)
        #print(computer_number)

        validation_result = validator.convert(player_choice)
        count += 1
        comparison_result = comparisator.compare(computer_number, validation_result, count)
        if comparison_result == True:
            more_suggestion = input('Do you want to play more? (Yes/No)')
            #print(more_suggestion)
            if more_suggestion.lower() == 'no':
                print('Goodbye!')
                break
            elif more_suggestion.lower() == 'yes':
                count = 0
                computer_number = random.randrange(1, 20, 1)
            else:
                print('Please, enter yes or no. The game restarted automaticaly, you may enter x to exit or n to restart again')
                
main()