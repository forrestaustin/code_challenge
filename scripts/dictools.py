""" Module of dictionary functions used by proccessdata, qwords, qusers"""

import pickle


def adduser_entry(user, userwords, usertoword_dict):
    """Updates a user to word list dictionary with new user tuple and corresponding list of words

    Takes in a dictionary that maps user uples to a list of words
    Takes in a user tuple (ip, ua)
    Takes in a list of words
    Returns updated dictionary with new user entry
    if no user given i.e. ("", ""), returns the original unmodified dictionary
    """
    new_udict = usertoword_dict
    if user in new_udict:
        prev_list = new_udict[user]
        updated_list = list(set(prev_list + userwords))
        new_udict[user] = updated_list
    else:
        new_udict[user] = userwords
    return new_udict


def addword_entry(user, userword_list, wordtouser_dict):
    """ Updates a word to user tuple dictionary with new word and corresponding user tuple
    Takes in a dictionary in form word -> [(ip1, ua1), (ip2, ua2)]
    Takes in a string for user
    Takes in a list of user tuples
    Returns the input dictionary with new word entry
    if no word given i.e. [], returns the original unmodified dictionary
    """
    if userword_list == []:
        return wordtouser_dict

    new_dict = wordtouser_dict
    for word in userword_list:
        if word in new_dict:
            prev_user_list = new_dict[word]
            updated_user_list = prev_user_list + [user]
            new_dict[word] = updated_user_list
        else:
            new_dict[word] = [user]
    return new_dict


def pickledict(dest_file, dictionary):
    """ uses pickle library to serialize a dictionary and store it in specified file location

    Takes in a string to file path destinaton
    Takes in a dictionary to be serialized
    """
    try:
        with open(dest_file, 'wb') as pickle_file:
            pickle.dump(dictionary, pickle_file)
    except IOError:
        print("unable to open file: ", dest_file)


def unpickle_dict(filename):
    """converts binary pickled dictionary back into text and loads into memory

    Takes in a filename and searches for that in the pickled_data folder
     Returns dictionary if found
     if not found, returns error
    """
    with open(filename, 'rb') as bfile:
        dictionary = pickle.load(bfile)
    return dictionary
