#Grades project

def grades(grade):
    if grade < 60:
        return 'F'
    elif 60 <= grade < 70:
        return 'D'
    elif 70 <= grade < 80:
        return 'C'
    elif 80 <= grade < 90:
        return 'B'
    elif grade >= 90:
        return 'A'

