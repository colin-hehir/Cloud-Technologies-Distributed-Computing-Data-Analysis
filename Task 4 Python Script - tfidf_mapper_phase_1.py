# These files were sourced from [1] which were modified from [2]. Changes were made by updating the ‘stop words’ with the ones in [3].
# [1] Vijay Khair, A. (2020). CA675_Cloud_Technologies_Assignment_1 [online] Available at: https://gitlab.computing.dcu.ie/khaira2/ca675_cloud_technologies_assignment_1
# [2] Patel, D. (2017). TF-IDF-implementation-using-map-reduce-Hadoop-python-  [online] Available at: https://github.com/devangpatel01/TF-IDF-implementation-using-map-reduce-Hadoop-python- 
# [3] RANKS NL. (2021). English Stopwords Available at: https://www.ranks.nl/stopwords
# Due to the consistent logic in the code, no other changes were made.

import sys
import os

stopwords= ['a','able','about','above','across','after','again','against','all','almost','also','am','among','an','and','any','are','as','at','be','because',
            'been','before','being','below','between','both','but','by','can','cannot','could','dear','did','do','does'','doing','down','during','each','either',
            'else','ever','every','few','for','from','further','get','got','had','has','have','he','her','hers','him','his','how','however','i','if','in','into',
            'is','it','its','just','least','let','like','likely','may','me','might','most','must','my','neither','no','nor','not','of','off','often','on','only',
            'or','other','our','own','rather','said','say','says','she','should','since','so','some','than','that','the','their','them','then','there','these',
            'they','this','tis','those','through','to','too','twas','under', 'until','us','wants','was','we','were','what','when','where','which','while','who',
            'whom','why','will','with','would','yet','you','your','yourself', 'yourselves'];

for line in sys.stdin:
   
    OwnerUserId, text = line.split(',', 1)
    text = text.strip()
    words = text.split()
    for word in words:
        word=word.lower();
        if word not in stopwords:
            z=word+' '+OwnerUserId;
            print '%s\t%s' % (z, 1)
        
        
