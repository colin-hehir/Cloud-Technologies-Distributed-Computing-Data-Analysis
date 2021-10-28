# These files were sourced from [1] which were modified from [2]. Changes were made by updating the ‘stop words’ with the ones in [3].
# [1] Vijay Khair, A. (2020). CA675_Cloud_Technologies_Assignment_1 [online] Available at: https://gitlab.computing.dcu.ie/khaira2/ca675_cloud_technologies_assignment_1
# [2] Patel, D. (2017). TF-IDF-implementation-using-map-reduce-Hadoop-python-  [online] Available at: https://github.com/devangpatel01/TF-IDF-implementation-using-map-reduce-Hadoop-python- 
# [3] RANKS NL. (2021). English Stopwords Available at: https://www.ranks.nl/stopwords
# Due to the consistent logic in the code, no other changes were made.

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None


for line in sys.stdin:
    line = line.strip()

    word, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue

    if current_word == word:
        current_count += count
    else:
        if current_word:
            print '%s\t%s' % (current_word, current_count)
        current_count = count
        current_word = word

if current_word == word:
    print '%s\t%s' % (current_word, current_count)
