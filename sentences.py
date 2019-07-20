import re
import numpy as np
import scipy.spatial as spatial

words = []
lines = []

with open('sentences.txt', 'r') as fin:
    for line in fin.readlines():
        res = [x for x in re.split('[^a-z]', line.lower()) if x]
        lines.append(res)
    
for line in lines:
    for word in line:
        if word in words: pass
        else: words.append(word)
        
np_words = np.zeros((len(lines), len(words)))
np_result = np.zeros(len(lines))
            
for i in range (0, len(lines)):
    for j in range(0, len(words)):
        np_words[i, j] = lines[i].count(words[j])

    np_result[i] = spatial.distance.cosine(np_words[0, :], np_words[i, :])
        
print np_result
