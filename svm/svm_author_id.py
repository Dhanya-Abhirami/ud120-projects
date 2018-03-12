#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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

### using a portion of the data set (smaller dataset => faster)
### comment this to see how SVM works on larger data sets (larger dataset => more accuracy)
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]
###

#########################################################
### your code goes here ###
from sklearn.svm import SVC
### try out kernel="linear" too
### take values of c=10.0, 100.0, 1000.0, 10000.0 etc to find best accuracy value
clf=SVC(C=10000.0,kernel="rbf")
t0=time()
clf.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"
t0=time()
pred = clf.predict(features_test)
print "predicting time:", round(time()-t0, 3), "s"
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(labels_test,pred)
print accuracy
### to see number of "1" predictions
#import numpy as np
#print np.count_nonzero(pred)
#########################################################

#Results : SVM is much slower than Naive Bayes
