#decision tree implementation

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree

def train_initial_data()->"a trained classifier based on trained data":
    data = np.genfromtxt("dataset2_random.txt", delimiter=",")
    Y = data[:, -1] #target value is last column
    X = data[:, 0:-1] #features are the other columns
    X_train, X_test, y_train, y_test = train_test_split(X,Y, test_size=0.3, random_state=100)
    clf_entropy = DecisionTreeClassifier(criterion="entropy", random_state=100,
                                         max_depth=3, min_samples_leaf=1)
    clf_entropy.fit(X_train, y_train) #Fit & train to the training set
    return clf_entropy

#retrain data and output clf
def retrain_data(text_file_name:str, clf:"classifier object")->"clf object retrained":
    pass

def prediction(clf: "classifier object", data: {'Time': int, 'Mood':int, 'Age':int}):
    '''Takes in a classifier and dict of data and outputs a number that represents
    the type of food they would want'''
    d=[[data['Time'],data['Mood'], data['Age']]]
    return clf.predict(d)

    
