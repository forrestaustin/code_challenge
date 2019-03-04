""" Module of parsing functions used by processdata to read and parse input txt"""

from urllib.parse import urlparse
import re


def entryparse(entry):
    """ function that searches an entry string for IP: UA: U: R:

    Takes in a string with the expected format of IP: <val1>\nUA: <val2>\nU: <val3>R: <val4>\n
    Returns a tuple containing all four values found (val1,val2,val3,val4)
    If not in pre-specified format, will return tuple of with empty strings for missing vals
    """

    try:
        ip = re.search(r'(?<=IP: ).*(?=\nUA:)', entry).group()
        ua = re.search(r'(?<=UA: ).*(?=\nU:)', entry).group()
        url = re.search(r'(?<=U: ).*(?=\nR:)', entry).group()
        ref = re.search(r'(?<=R: ).*(?=\n)', entry).group()
        sub_entries = (ip, ua, url, ref)
        return sub_entries
    except:  # would occur if entry does not fit predefined format
        print("Invalid data entry found")
        return("", "", "", "")


def filter_func(token):
    """Used with filter() function to filter out the following list items

    Also filters out entries that are are digits i.e. "76120"
    """

    filter_list = ['com', 'org', 'net', 'html', 'php', '', 'www']  # words to remove
    if token in filter_list:
        return False
    elif token.isdigit():      # removes words that are all digits
        return False
    else:
        return True


def urltowords(url):
    """Breaks down a url-like string into a list of tokens or words

    Takes in a string and breaks it up into its url components ()

    If not a component can not be found it will be empty string
    Currently, ignoring query and parameter portions of the string

    Returns a list of words of the tokenized input string
    """

    if url == '':               # occurs when entry string in invalid format
        return []

    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    path = parsed_url.path
    params = parsed_url.params  # currently not using
    sub_url = domain + path     # can include in sub_url to also tokenize parameters

    # replace delimiters with "/" and split string just by "/"
    delimiters = ['.', '|', ';', '?', '+', "=", '\\']
    for delim in delimiters:
        sub_url = sub_url.replace(delim, '/')

    url_tokens = sub_url.split("/")

    # if a token contains "-" then make entry for original and sub-tokens
    for token in url_tokens:
        if "-" in token:
            subtokens = token.split("-")
            url_tokens = subtokens + url_tokens

    filtered_tokens = filter(filter_func, url_tokens)
    return list(set(filtered_tokens))
