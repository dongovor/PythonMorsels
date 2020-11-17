import sys
import os

file_name = sys.argv[1]
out_file = sys.argv[2]
fp = open(file_name)
content = fp.read()
content = content.replace('|', ',')

fp = open(out_file, 'w')
fp.write(content)
fp.close()