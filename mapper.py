
import sys
l_num = 0
for line in sys.stdin:
    l_num += 1
    line = line.strip()
    words = line.split()
    if len(line) > 1:
        for word in words:
            print('%s\t%d\t%d' % (word, 1, l_num))