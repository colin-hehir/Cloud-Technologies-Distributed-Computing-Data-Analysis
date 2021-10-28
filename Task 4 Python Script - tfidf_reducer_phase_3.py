# These files were sourced from [1] which were modified from [2]. Changes were made by updating the ‘stop words’ with the ones in [3].
# [1] Vijay Khair, A. (2020). CA675_Cloud_Technologies_Assignment_1 [online] Available at: https://gitlab.computing.dcu.ie/khaira2/ca675_cloud_technologies_assignment_1
# [2] Patel, D. (2017). TF-IDF-implementation-using-map-reduce-Hadoop-python-  [online] Available at: https://github.com/devangpatel01/TF-IDF-implementation-using-map-reduce-Hadoop-python- 
# [3] RANKS NL. (2021). English Stopwords Available at: https://www.ranks.nl/stopwords
# Due to the consistent logic in the code, no other changes were made.

from operator import itemgetter
import sys

prev_word = None
count = 1 
word = None
df={}
l1=[]

for line in sys.stdin:
    line = line.strip()
    w,z= line.split('\t', 1)
    f,nNc = z.split(' ',1)
    n,Nc=nNc.split(' ',1)
    N,c=Nc.split(' ',1)
    if prev_word == w:
        count = count+int(c)
    else:
        if prev_word != None:
            q=n+' '+N+' '+str(count)
            df[prev_word]=q
            j=prev_word+' '+f
            l1.append(j)
        count=1
        prev_word = w

       
q=n+' '+N+' '+str(count)
df[prev_word]=q
j=prev_word+' '+f
l1.append(j)

for h in l1:
   w,f=h.split(' ',1)
   for d in df:
       if w == d:
          print '%s\t%s' % (h,df[d])
