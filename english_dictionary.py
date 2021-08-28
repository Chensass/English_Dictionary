import json
from difflib import get_close_matches
from termcolor import colored


def get_word_meaning_from_dict(dictionary_data, user_input):
    """
    This fucntion takse a user input string and returns the word meaning from dictionary.
    :param dictionary_data: loaded json file to dict
    :param user_input: string input user inserted
    :return: list of user_input meanings from dictionary
    """
    try:
        if user_input in dictionary_data:
            for meaning in dictionary_data[user_input]:
                print(meaning)
            return dictionary_data[user_input]
        elif user_input.title() in dictionary_data:
            for meaning in dictionary_data[user_input.title()]:
                print(meaning)
            return dictionary_data[user_input.title()]
        elif user_input.upper() in dictionary_data:
            for meaning in dictionary_data[user_input.upper()]:
                print(meaning)
            return dictionary_data[user_input.upper()]
        elif get_close_matches(user_input, dictionary_data.keys(), n=1, cutoff=0.85):
            corrected_word = get_close_matches(user_input, dictionary_data.keys(), n=1, cutoff=0.85)[0]
            correction_input = input(f'Did you mean {corrected_word}? If yes type : Y , if not type: N.')
            correct_input_name(dictionary_data, user_input, correction_input)
        else:
            print(colored('Error!: key error, try another word.', 'blue'))
    except:
        print(colored('Error!: key error,this word dosnt exist in dictionary, please insert another word.'))


def correct_input_name(dictionary_data, user_input, correction_input):
    """
    This function corrects the user input word to the closest one founded in dictionary and returns its meaning.
    :param dictionary_data: loaded json file to dict
    :param user_input:  string input user inserted
    :param correction_input: the corrected user input word
    :return: returns the corrected inserted words meaning from dictionary.
    """
    corrected_word = get_close_matches(user_input, dictionary_data.keys(), n=1)[0]
    if correction_input == 'Y':
        if len(dictionary_data[corrected_word]) > 1:
            for meaning in dictionary_data[corrected_word]:
                print(meaning)
        else:
            print(dictionary_data[corrected_word])
        return dictionary_data[corrected_word]
    else:
        print(colored('Error!: key dosnt match Y or N, please enter word again.', 'blue'))


def main():
    while True:
        dictionary_data = json.load(open("data.json"))
        user_input = input('Insert word: ').lower()
        get_word_meaning_from_dict(dictionary_data, user_input)



if __name__=='__main__':
    main()