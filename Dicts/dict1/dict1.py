def create_dict_from_lists(keys, values):
    """
    This function returns a dict made from two lists.
    """
    #pass  # implement me
    return dict(zip(keys,values))

def merge_two_dicts(d1, d2):
    """
    Merge two Python dictionaries into one
    """
    d1.update(d2)
    return d1

def init_dict_with_values(lst, d1):
    """
    Create a dict with default values for each key listed.

    """
    #
    return {i:d1 for i in lst}

def extract_keys_to_dict(datadict, keylist):
    """
    Create a dictionary by extracting the keylist from a given dictionary
    """
    #
    # a = {i:j for i, j in datadict, keylist if datadict.keys() in keylist }
    return {i : datadict[i] for i in keylist if i in datadict }

def delete_keys_from_dict(datadict, keylist):
    """
    Delete a list of keys from a dictionary
    """
    return {i : datadict[i] for i in datadict.keys() if i not in keylist }

def check_dict_for_key(datadict, key):
    """
    Check if a value exists in a dictionary
    (NO FOR loops!)
    """
    return key in datadict.values()

def get_key_of_min_value(ddd):
    """
    Get the key of the minimum value from a dictionary
    """
    return min(ddd, key = ddd.get)
    

def get_key_of_max_value(ddd):
    """
    Get the key of the maximum value from a dictionary
    """
    return max(ddd, key = ddd.get)