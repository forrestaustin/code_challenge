"""
Set of parameterized unit tests for testing functionality of  dictools

some common test cases were adding a user or word entry to empty dictionary
adding to a non empty dictionary
adding to non empty dictionary that already has a key

"""
import pytest
from scripts.dictools import addword_entry
from scripts.dictools import adduser_entry


utw_dict_1 = {("ip1", "ua1" ):['nasa']}
utw_dict_2 = {("192.168", "Mozilla user"):["word1", "word2", "word3"]}
empty_dict = {}


@pytest.mark.parametrize(
    'user_tuple, wordlist, input_dict, output_dict', [
        (("forrest", "uastring"), ['cat','dog'], {}, {("forrest", "uastring"):['cat','dog']}),
        (("john", "graham"), [], {("ip2", "ua2"):['cat','dog']}, {("john", "graham"):[], ("ip2", "ua2"):['cat','dog']}),
        (("ip1", "ua1"), ['space'], utw_dict_1, {("ip1", "ua1"):['nasa', 'space']})
    ]
)
def test_adduser_entry(user_tuple, wordlist, input_dict, output_dict):
    """ In order to test if the entry was added correctly, must compare the sets of input/ output dictionaries
    This is because it will return False if the same word lists contain the same words in different order
    """

    assert set(adduser_entry(user_tuple, wordlist, input_dict)[user_tuple]) == set(output_dict[user_tuple])
    for key in output_dict:
        assert type(key) == tuple
        assert type(output_dict[user_tuple]) == list


@pytest.mark.parametrize(
    'user_tuple, wordlist, input_dict, output_dict', [
        (("ip", "ua"), ['cat','dog'], {}, {"cat":[("ip", "ua")], "dog":[("ip", "ua")]}),
        (("john", "graham"), [], {}, {}),
        (("ip1", "ua1"), ['space'], {'space':[('ip2','ua2')]}, {"space":[("ip1","ua1"), ("ip2", "ua2")]})
    ]
)
def test_addword_entry(user_tuple, wordlist, input_dict, output_dict):
    """ Function checks to see if the user tuple was added to each of the word entries in word list

    """
    for word in wordlist:
        assert user_tuple in addword_entry(user_tuple, wordlist, input_dict)[word]
