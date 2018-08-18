
import sys
wordcount = {}
l = 1
for line in sys.stdin:
    line = line.strip()
    word, count, l_num = line.split('\t')
    try:
        count = int(count)
        l_num = int(l_num)
    except ValueError:
        continue
    if word not in wordcount:
        wordcount[word] = {}
        wordcount[word]["count"] = count
        wordcount[word]["line"] = [l_num]
    else:
        wordcount[word]["count"] += count
        wordcount[word]["line"].append(l_num)
for w, arr in wordcount.items():
    print (' %d %s  %s' % (arr["count"], w, " ".join(str(x) for x in arr["line"])))