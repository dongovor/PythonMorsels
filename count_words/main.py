def count_words(in_str):
    in_str = in_str.lower()
    out_dict = {}

    for word in in_str.split():
        if word in out_dict:
            out_dict[word] += 1
        else:
            out_dict[word] = 1
    return out_dict