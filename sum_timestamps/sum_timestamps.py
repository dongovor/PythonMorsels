import datetime

def sum_timestamps(in_list):
    out_time = datetime.timedelta()
    for i in in_list:
        if len(i.split(":")) < 3:
            (m, s) = i.split(':')
            t  = datetime.timedelta(minutes=int(m), seconds=int(s))
            out_time += t
        else:
            (h, m, s) = i.split(':')
            t  = datetime.timedelta(hours = int(h), minutes=int(m), seconds=int(s))
            out_time += t
    if str(out_time).split(':')[1][0] == '0':
        print('a')
        return ':'.join(str(out_time).split(':')[1:3])[1:]
    else:
        return ':'.join(str(out_time).split(':')[1:3])

#print(sum_timestamps(['15:32', '45:48']))
print(sum_timestamps(['02:01']), '2:01')
