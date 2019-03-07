""" Module that queries a dictionary by user and returns list of associated words

Takes in two command line arguments of the form IP Address "User agent String"
Currently, user queries are case sensitive
The dictionary it queries is loaded from data/pickled_data/wtu_dict.pickle

Returns list of words found for that user
Return error if the wtu_dict.pickle can not be located
"""

import os
import sys
from scripts.dictools import unpickle_dict
import argparse

#test_val = ("76.125.188.56", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:9.0.1) Gecko/20100101 Firefox/9.0.1")

def main(userquery):

    scriptspath = os.path.dirname(__file__)
    datapath_pickle = os.path.join(scriptspath, "..", "data", "pickled_data")
    utw_path = os.path.join(datapath_pickle, "utw.pickle")

    try:
        utw_dict = unpickle_dict(utw_path)
    except:
        print("Error unpickling file: ", utw_path)
        print("Run scripts.processdata to generate pickle file ")
        sys.exit(1)

    if userquery in utw_dict:
        result_list = utw_dict[userquery]
        for word in result_list:
            print(word)
    else:
        result_list = None
        print("No words found for: ", userquery)

    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Input a user tuple to query corresponding words')
    parser.add_argument("user_ip", help='user ip address to be searched')
    parser.add_argument("user_ua", help='user agent string to be searched for')
    args = parser.parse_args()
    userip = args.user_ip
    userua = args.user_ua
    usertup = (userip, userua)
    rv = main(usertup)
    sys.exit(rv)  # 0 if script executed without errors
