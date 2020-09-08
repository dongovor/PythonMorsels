import string

def is_anagram(in_str1, in_str2):
    in_str1 = in_str1.translate(str.maketrans('', '', string.punctuation)).replace(' ','')
    in_str2 = in_str2.translate(str.maketrans('', '', string.punctuation)).replace(' ','')
    if sorted(in_str1.lower().strip()) == sorted(in_str2.lower().strip()):
        return True
    else:
        return False

print(is_anagram("cardiografía", "radiográfica"))