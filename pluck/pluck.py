def pluck(dictionary, key_path):
    """Deep-query a dictionary"""
    keys = key_path.split('.')[::-1]
    value = dictionary
    while keys:
        value = value[keys.pop()]
    return value