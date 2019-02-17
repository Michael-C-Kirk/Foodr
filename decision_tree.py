import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree





if __name__ == "__main__":
    data = np.genfromtxt("dataset1.txt", delimiter=",")
    Y = data[:, -1] #target value is last column
    X = data[:, 0:-1] #features are the other columns

    numSamples, numFeatures = X.shape
    print("number of samples:", numSamples, "\nnumber of features:", numFeatures)

    X_train, X_test, y_train, y_test = train_test_split(X,Y, test_size=0.3, random_state=100)

    
