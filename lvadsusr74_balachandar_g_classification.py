# -*- coding: utf-8 -*-
"""LVADSUSR74-Balachandar_G-Classification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qjgEgx0kc50VgYnpgk95SryMGvawkGlQ
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import IsolationForest
from sklearn.metrics import accuracy_score,f1_score,recall_score,confusion_matrix
from sklearn.preprocessing import LabelEncoder

#Reading the CSV file using Pandas
df = pd.read_csv("/content/drive/MyDrive/Datasets_file/penguins_classification.csv")
df.info()

df.isnull().sum()
df.fillna(method='ffill',inplace =True)
df.fillna(method = 'bfill',inplace = True)

df.duplicated().sum()

#checking for outliers using boxplot
plt.figure(figsize=(20,10))
sns.boxplot(data = df)
plt.title("Identifying the outliers")
plt.show()

#Removing Outliers Using Isolation Forest
df_55=pd.DataFrame(df)
iso = IsolationForest(contamination=0.1)
outliers = iso.fit_predict(df_55['bill_length_mm'].values.reshape(-1,1))
dd=df.drop(df_55.iloc[np.where(outliers== -1)].index,inplace=False)
dd.info()

#checking for outliers using boxplot after removing the outliers
plt.figure(figsize=(20,10))
sns.boxplot(data = dd)
plt.title("After Removing the outliers")
plt.show()

#dropping the unwanted columns
dd.drop("island",axis =1,inplace=True)
dd.drop("body_mass_g",axis=1,inplace =True)
dd.drop("year",axis=1,inplace =True)

dd.info()

#Converting the categorical to Numerical Values
label_encoder = LabelEncoder()
dd["species"] = label_encoder.fit_transform(dd["species"])
dd.head()

X = dd[["bill_length_mm","bill_depth_mm","flipper_length_mm"]]
y = dd["species"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3,random_state =42)

#DecisionTreeClassifier
clf_Dt = DecisionTreeClassifier()
clf_Dt.fit(X_train,y_train)
a_Dt = clf_Dt.predict(X_test)
Decision_accuracy_score = accuracy_score(y_test,a_Dt)
print(Decision_accuracy_score)
Decision_recall_score = recall_score(y_test,a_Dt)
print(Decision_recall_score)
Decision_f1_score = f1_score(y_test,a_Dt)
print(Decision_f1_score)




#Insights
#The Decision Tree classifier provides the acuurate classification of the penguins based on the feature SelectionRangeSlider
#bill morphology and flipper length