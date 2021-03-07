import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score


class svmModel:

    def __init__(self, data):

        print("Generating Model")
        self.dataset = pd.read_csv(data)
        self.dataset = self.dataset.drop(self.dataset.columns[[0]], axis=1)
        self.numChannels = 8
        self.nDataSetLength = len(self.dataset)


        #K values should be sqrt(N)
        if math.sqrt(self.nDataSetLength) % 2 == 0:
            self.k = int(math.sqrt(self.nDataSetLength)) + 1
        else:
            self.k = int(math.sqrt(self.nDataSetLength))

        self.X = self.dataset.iloc[:, 0:self.numChannels]
        self.Y = self.dataset.iloc[:, self.numChannels]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.Y, random_state=0, test_size=0.2)

        self.sc_X = StandardScaler()
        self.X_train = self.sc_X.fit_transform(self.X_train)
        self.X_test = self.sc_X.transform(self.X_test)

        self.classifier = KNeighborsClassifier(n_neighbors=self.k*2, p=2, metric='euclidean')
        self.classifier.fit(self.X_train,self.y_train)

        self.y_pred = self.classifier.predict(self.X_test)
        print("Model Generated")
        #print(self.X)
        #print(self.X_train)

        #evaluate the model
        #self.cm = confusion_matrix(self.y_test,self.y_pred)
        #print(cm)
        print(f1_score(self.y_test,self.y_pred))
        print(accuracy_score(self.y_test,self.y_pred))
