def with_previous(in_text):
    prev_symbol = None
    tmp_tuple = ()
    out_coll = []
    
    for letter in in_text:
        tmp_tuple = (letter, prev_symbol)
        out_coll.append(tmp_tuple)
        tmp_tuple = ()
        prev_symbol = letter
    
    return out_coll

print(with_previous("hello"))