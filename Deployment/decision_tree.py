#decision tree implementation

import numpy as np
import data_update #our module
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree



def train_initial_data(text_file_name:str)->"a trained classifier based on trained data":
    data = np.genfromtxt(text_file_name, delimiter=",")
    Y = data[:, -1] #target value is last column
    X = data[:, 0:-1] #features are the other columns
    #X_train, X_test, y_train, y_test = train_test_split(X,Y, test_size=0.3, random_state=100)
    clf_entropy = DecisionTreeClassifier(criterion="entropy", random_state=100,
                                         max_depth=3, min_samples_leaf=1)
    clf_entropy.fit(X, Y) #Fit & train to the training set
    return clf_entropy

#retrain data and output clf
def retrain_data(text_file_name:str, clf:"classifier object")->"clf object retrained":
    data = np.genfromtxt(text_file_name, delimiter=",")
    Y = data[:, -1] #target value is last column
    X = data[:, 0:-1] #features are the other columns
    clf.fit(X,Y)
    #data_update.update_data_set()
    return clf

def prediction(clf: "classifier object", data: {'Time': int, 'Mood':int, 'Age':int}):
    '''Takes in a classifier and dict of data and outputs a number that represents
    the type of food they would want'''
    d=[[data['Time'],data['Mood'], data['Age']]]
    return clf.predict(d)


##if __name__ == "__main__":
##    clf = train_initial_data()
##    data_update.update_data_set("example_data.txt", {"Time":1,"Mood":1,"Age":1},4)
##    retrain_data("example_data.txt", clf)
##    print(clf.predict([[1,0,1]]))
