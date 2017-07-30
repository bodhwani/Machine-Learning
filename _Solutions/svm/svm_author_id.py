#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.metrics import accuracy_score
from time import time


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()



features_train = features_train[:len(features_train)/100] 
labels_train = labels_train[:len(labels_train)/100] 

#########################################################
### your code goes here ###
from sklearn import svm
print("#####3Started")
clf = svm.SVC(kernel = 'rbf',C=10000)


t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"


print("#####training completed")

t0 = time()
pred = clf.predict(features_test)
print "training time:", round(time()-t0, 3), "s"

print("Here is the pred",pred)
c,s=0,0
for i in pred:
    if(i==1):
        c=c+1
    else:
        s=s+1
print("Value for c is ",c)
print("Value for s is ",s)

#print("The class of SVM(0 for A and 1 for B) predict for element 10th,26th and 50th is\n")
#ans10= pred[10]
#print('For 10th element:',ans10)
#
#ans26= pred[26]
#print('For 26th element:',ans26)
#
#ans50= pred[50]
#print('For 50th element:',ans50)

#accuracy = accuracy_score(pred, labels_test)
#print("Here is the new accuracy",accuracy)


#########################################################


