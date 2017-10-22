#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below


for point in data:
    salary = point
    bonus = point
    
    matplotlib.pyplot.scatter( salary, bonus )

for i in data:
    
    if(i[0]>1000000 and i[1]>500000  ):
        print i

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
