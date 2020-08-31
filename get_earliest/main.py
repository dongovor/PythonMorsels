def get_earliest(date1, date2):
    (md1, dd1, yd1) = date1.split('/')
    (md2, dd2, yd2) = date2.split('/')
    print(md1 + dd1 + yd1)
    print(md2 + dd2 + yd2)
    return date1 if (yd1, md1, dd1) < (yd2, md2, dd2) else date2

print(get_earliest('02/29/1972', '12/21/1946'))