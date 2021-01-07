import pandas as pd
import numpy as np
import math

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score

dataset = pd.read_csv('Data.csv')

nDataSetLength = len(dataset)

X = dataset.iloc[:, 0:2].values
Y = dataset.iloc[:, 2].values

X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state=0, test_size=0.2)

sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

classifier = KNeighborsClassifier(n_neighbors=6, p=2, metric='euclidean')
classifier.fit(X_train,y_train)

y_pred = classifier.predict(X_test)


#evaluate the model
cm = confusion_matrix(y_test,y_pred)
#print(cm)
#print(f1_score(y_test,y_pred))
#print(accuracy_score(y_test,y_pred))
newData = pd.read_csv('new.csv')
X = newData.iloc[:, 0:2].values
newXTest = sc_X.transform(X)

prediction = classifier.predict(newXTest)
print(prediction)
