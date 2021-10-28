# These files were sourced from [1] which were modified from [2]. Changes were made by updating the ‘stop words’ with the ones in [3].
# [1] Vijay Khair, A. (2020). CA675_Cloud_Technologies_Assignment_1 [online] Available at: https://gitlab.computing.dcu.ie/khaira2/ca675_cloud_technologies_assignment_1
# [2] Patel, D. (2017). TF-IDF-implementation-using-map-reduce-Hadoop-python-  [online] Available at: https://github.com/devangpatel01/TF-IDF-implementation-using-map-reduce-Hadoop-python- 
# [3] RANKS NL. (2021). English Stopwords Available at: https://www.ranks.nl/stopwords
# Due to the consistent logic in the code, no other changes were made.

import sys
import os
from math import log,sqrt

D=10.0

for line in sys.stdin:
    line = line.strip()
    wf,nNm=line.split('\t',1)
    word, file = wf.split(' ',1)
    n,N,m=nNm.split(' ',2)
    n=float(n)
    N=float(N)
    m=float(m)
    tfidf= (n/N)*log(D/m)
    print '%s\t%s\t%s' % (word,file,round(tfidf,6))

        
