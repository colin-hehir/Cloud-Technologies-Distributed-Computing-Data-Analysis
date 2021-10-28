# These files were sourced from [1] which were modified from [2]. Changes were made by updating the ‘stop words’ with the ones in [3].
# [1] Vijay Khair, A. (2020). CA675_Cloud_Technologies_Assignment_1 [online] Available at: https://gitlab.computing.dcu.ie/khaira2/ca675_cloud_technologies_assignment_1
# [2] Patel, D. (2017). TF-IDF-implementation-using-map-reduce-Hadoop-python-  [online] Available at: https://github.com/devangpatel01/TF-IDF-implementation-using-map-reduce-Hadoop-python- 
# [3] RANKS NL. (2021). English Stopwords Available at: https://www.ranks.nl/stopwords
# Due to the consistent logic in the code, no other changes were made.

from operator import itemgetter
import sys

current_word = None
prev_filename = None
current_count = 0
word = None
N=0
df={}
l1=[]


for line in sys.stdin:
    line = line.strip()
    l1.append(line)
    filename,wordcount = line.split('\t', 1)
    word,count = wordcount.split(' ', 1)
    count=int(count)
    if prev_filename == filename:
        N=N+count
    else:
       if prev_filename != None:
            df[prev_filename]=N
       N=0
       prev_filename = filename
df[prev_filename]=N


for h in l1:
    filename,wordcount = h.split('\t', 1)
    word,count = wordcount.split(' ', 1) 
    for k in df:
        if filename == k:
           wf=word+' '+filename
           nN=count+' '+str(df[k])
           print '%s\t%s' % (wf,nN)
    
