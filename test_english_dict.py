from english_dictionary import get_word_meaning_from_dict, correct_input_name
import json
from difflib import get_close_matches

dictionary_data = json.load(open("data.json"))


def test_func_get_word_meaning_from_dict_():
    assert get_word_meaning_from_dict(dictionary_data, user_input='rain') == \
           ['Precipitation in the form of liquid water drops with diameters greater than 0.5 millimetres.',
            'To fall from the clouds in drops of water.']
    assert get_word_meaning_from_dict(dictionary_data, user_input='paris') == \
           ['The capital and largest city of France.']
    assert get_word_meaning_from_dict(dictionary_data, user_input='usa') == \
           ['A country and federal republic in North America located north of Mexico and south of Canada,'
            ' including Alaska, Hawaii and overseas territories.']



def test_func_correct_input_name():
    assert correct_input_name(dictionary_data, user_input='rainn',
                              correction_input='Y') == \
                            ['Precipitation in the form of liquid water drops with diameters greater than 0.5 millimetres.',
                             'To fall from the clouds in drops of water.']