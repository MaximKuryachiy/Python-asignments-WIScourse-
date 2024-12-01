def compare(computer_number, validation_result, count):
        if computer_number < validation_result:
            print('Try a smaller number')
            return False
        elif computer_number > validation_result:
            print('Try a bigger number')
            return False
        elif computer_number == validation_result:
            print('Congratulations, you won! :) It took you', count, 'guesses.')
            return True