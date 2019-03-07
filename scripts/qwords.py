""" Module that queries a dictionary by word and returns list of associated user tuples

Takes in a command line argument word. If multiple words are entered only the first will be used.
Currently, query words or case sensitive
The dictionary it queries is loaded from data/pickled_data/wtu_dict.pickle

Returns list of user tuples found for that word.
Return error if the wtu_dict.pickle can not be located
"""

import os
import sys
from scripts.dictools import unpickle_dict
import argparse


def main(wordquery):

    scriptspath = os.path.dirname(__file__)
    datapath_pickle = os.path.join(scriptspath, "..", "data", "pickled_data")
    wtu_path = os.path.join(datapath_pickle, "wtu.pickle")

    try:
        wtu_dict = unpickle_dict(wtu_path)
    except:
        print("Error unpickling file: ", wtu_path)
        print("Run scripts.processdata to generate pickle file ")
        sys.exit(1)

    if wordquery in wtu_dict:
        result_list = wtu_dict[wordquery]
        for user in result_list:
            print(user)
    else:
        result_list = None
        print("No users found for: ", wordquery)

    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Input a word to query user to word dictionary')
    parser.add_argument("wordinput", help='word to be searched for')
    args = parser.parse_args()
    word = args.wordinput
    rv = main(word)
    sys.exit(rv)  # 0 if script executed without errors