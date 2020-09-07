def semantic_wrap(in_str):
    PUNKT_CHAR = ('.', '?', '!')
    for p_char in PUNKT_CHAR:
        in_str = in_str.replace(f'{p_char}  ', f'{p_char}\n')
        in_str = in_str.replace(f'{p_char} ', f'{p_char}\n')
    return in_str