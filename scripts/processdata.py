""" Module that parses a given text file into two dictionaries then stores them as binary files

Takes in required command line argument of path to txt file with data
Returns error if file provided cannot be opened

Output is two pickled dictionaries in data/pickled_data folder
utw.pickle is dictionary mapping users to a list of words parsed from U: and R: entries
wtu.pickle is dictionary that maps a word that has been parsed to the corresponding user tuple

"""
from scripts.parsetools import entryparse
from scripts.parsetools import urltowords
from scripts.dictools import adduser_entry
from scripts.dictools import addword_entry
from scripts.dictools import pickledict
import os
import sys
import argparse
import re

ip_p = re.compile(r'(?<=IP: ).*(?=\nUA:)')
ua_p = re.compile(r'(?<=UA: ).*(?=\nU:)')
url_p = re.compile(r'(?<=U: ).*(?=\nR:)')
ref_p = re.compile(r'(?<=R: ).*(?=\n)')

def main(filepath):

    entry = ""
    utw_dict = {}
    wtu_dict = {}

    scriptspath = os.path.dirname(__file__)
    datapath_pickle = os.path.join(scriptspath, "..", "data", "pickled_data")

    utw_filepath = os.path.join(datapath_pickle, "utw.pickle")
    wtu_filepath = os.path.join(datapath_pickle, "wtu.pickle")

# entry is string that captures lines between ****\n and resets to "" empty string after encountering ****
    with open(filepath, encoding="utf8") as rawdata:  # file must be in raw_data folder
        for line in rawdata:
            if "****\n" in line and entry is not "":
                entry_tuple = entryparse(entry)

                user_tuple = (entry_tuple[0], entry_tuple[1])
                userwords_list = list(set(urltowords(entry_tuple[2]) + urltowords(entry_tuple[3])))
                utw_dict = adduser_entry(user_tuple, userwords_list, utw_dict)
                wtu_dict = addword_entry(user_tuple, userwords_list, wtu_dict)
                entry = ""
            elif "****\n" in line:
                continue
            else:
                entry += line

    pickledict(utw_filepath, utw_dict)
    pickledict(wtu_filepath, wtu_dict)

    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Take in a file path to txt file')
    parser.add_argument("filepath", help='the path to an input txt file')
    args = parser.parse_args()
    filepath = args.filepath
    rv = main(filepath)
    sys.exit(rv)  # 0 if script executed without errors
