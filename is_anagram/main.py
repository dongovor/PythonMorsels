import string

def is_anagram(in_str1, in_str2):
    in_str1 = in_str1.translate(str.maketrans('', '', string.punctuation)).replace(' ','')
    in_str2 = in_str2.translate(str.maketrans('', '', string.punctuation)).replace(' ','')  
    return sorted(in_str1.lower()) == sorted(in_str2.lower())