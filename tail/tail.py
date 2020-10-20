#
def tail(in_value, n):
    if n <= 0:
        return []
    else:      
        if isinstance(in_value, str):
            return (list(in_value))[-n:]
        else:
            return (list(in_value))[-n:]