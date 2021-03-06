# -*- coding: utf-8 -*-
"""HackUMBC2020

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ozf6p5ilA2xVHnA0hJUUchCZ2CDvVyMI
"""

#install them dependencies

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix

#Load the data
from google.colab import files
uploaded = files.upload()

#load the data to dfraud
dfraud = pd.read_csv("hackUMBC_CC_fraud_detection_AllNumbers_refined.csv")

#take a looksy at the data; "Is_declined, isForeignTransaction, isHighRiskCountry, isFradulent" - have either 1 or 0, 1 = yes and 0 = no
dfraud.head()

#another looksy at the data
dfraud.sample

#split dataset in features and target variable
feature_cols = ['Transaction_amount', 'Is_declined', 'Total_number_of_declines/day', 'isForeignTransaction', 'isHighRiskCountry'] 
X = dfraud[feature_cols] # Features
Y = dfraud.isFradulent # Target variable

# split X and Y into training and testing sets
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.25,random_state=0)

# import the class and create classifier/model
from sklearn.neural_network import MLPClassifier
model = MLPClassifier(hidden_layer_sizes=(30, 30, 20),activation='relu',random_state=101)

#train that model
model.fit(X_train, Y_train)

#predict
Y_predict = model.predict(X_test)

# import confusion_matrix and classification_report classes
from sklearn.metrics import classification_report, confusion_matrix

#computer performance measures
print(confusion_matrix(Y_test, Y_predict))  
print(classification_report(Y_test, Y_predict))

from sklearn import metrics
#Calculate performance measures:
print("Accuracy:",metrics.accuracy_score(Y_test, Y_predict))
print("Precision:",metrics.precision_score(Y_test, Y_predict))
print("Recall:",metrics.recall_score(Y_test, Y_predict))

# import required modules
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class_names=[0,1] # name  of classes
fig, ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)

# create heatmap
cnf_matrix =confusion_matrix(Y_test, Y_predict)
sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="YlGnBu" ,fmt='g')
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Confusion matrix', y=1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')





