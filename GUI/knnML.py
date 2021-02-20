import pandas as pd
import numpy as np
import math

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score

class KNN():

    def __init__(self, data):

        self.dataset = data
        self.numChannels = 8
        self.nDataSetLength = len(self.dataset)

        #K values should be sqrt(N)
        if sqrt(self.nDataSetLength) % 2 == 0:
            self.k = int(sqrt(self.nDataSetLength)) + 1
        else:
            self.k = int(sqrt(self.nDataSetLength))

        self.X = self.dataset.iloc[:, 0:self.numChannels].values
        self.Y = self.dataset.iloc[:, self.numChannels].values

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.Y, random_state=0, test_size=0.2)

        self.sc_X = StandardScaler()
        self.X_train = self.sc_X.fit_transform(X_train)
        self.X_test = self.sc_X.transform(X_test)

        self.classifier = KNeighborsClassifier(n_neighbors=self.k, p=2, metric='euclidean')
        self.classifier.fit(X_train,y_train)

        #y_pred = classifier.predict(X_test)


        #evaluate the model
        self.cm = confusion_matrix(y_test,y_pred)
        #print(cm)
        #print(f1_score(y_test,y_pred))
        #print(accuracy_score(y_test,y_pred))
