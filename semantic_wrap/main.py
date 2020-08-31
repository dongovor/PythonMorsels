def semantic_wrap(in_str):
    out_str = ''
    for i in in_str.split('. '):
        out_str += f'{i}\n'
    return out_str

print(semantic_wrap("Sentence one. Sentence two. Sentence three."))