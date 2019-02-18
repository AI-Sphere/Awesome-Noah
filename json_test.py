# -*- coding: UTF-8 -*-.
from __future__ import print_function
import json

cv = './AIMaintainable/cv.json'
nlp = './AIMaintainable/nlp.json'
dm = './AIMaintainable/data_mining.json'
ongoing = './AIMaintainable/ongoing.json'

p_list = [cv, nlp, dm, ongoing]
for p in p_list:
    try:
        json.load(open('%s' % p))
    except:
        print("JSON FORMAT ERROR: please check your %s file." % p)
        exit(1)

print('[GOOD JOB]: Passed All JSON FORMAT Test')