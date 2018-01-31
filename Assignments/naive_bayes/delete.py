#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 15:47:15 2017

@author: Vinit
"""

#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
print "features_test is ",features_test
print "features_train is ",features_train
print "labels_test is ",labels_test
print "labels_train is ",labels_train




#########################################################
### your code goes here ###

import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

clf = GaussianNB()

t0 = time()


clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"


t0 = time()
pred = clf.predict(features_test)
print "This is prediction",pred
print "prediction time:", round(time()-t0, 3), "s"


accuracy = accuracy_score(pred, labels_test)
print("Here is the accuracy",accuracy)
#########################################################
#Output :
#no. of Chris training emails: 7936
#no. of Sara training emails: 7884
#training time: 2.582 s
#prediction time: 0.223 s
#('Here is the accuracy', 0.97326507394766781)
    


