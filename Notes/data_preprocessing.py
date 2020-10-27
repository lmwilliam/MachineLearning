# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 22:27:49 2020

@author: WilliamLiang
"""

import numpy as np
import pandas as pd


# In[1] Load Dataset
dataset = pd.read_csv("CarEvaluation.csv")

# In[2] Decomomsition X(Independent Variable) & Y(Controlled Variable)
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, -1].values

# In[3] How to detect the missing data?

# 1.DataFrame format
print(dataset.isnull(),"\n")

# 2.Series format
print(dataset.isnull().sum(),"\n")
print(dataset.isnull().any(),"\n")

# 3.Counting the missing data
print(sum(dataset.isnull().sum()))

# In[4] Missing data imputing method
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
imputer = imputer.fit(X[:, 1:4])
X[:, 1:4] = imputer.transform(X[:, 1:4])

# In[5] Lebel Encoder
from sklearn.preprocessing import LabelEncoder

labelEncoder = LabelEncoder()
Y = labelEncoder.fit_transform(Y).astype("float64")

# In[6] One-Hot Encoder

ary_dummies = pd.get_dummies(X[:,0]).values
X = np.concatenate((ary_dummies, X[:,1:4]), axis=1).astype("float64")

# In[7] Split training and testing dataset
from sklearn.model_selection import train_test_split

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=0)

# In[8] Feature Scaling
from sklearn.preprocessing import StandardScaler

sc_X = StandardScaler().fit(X_train)
X_train = sc_X.transform(X_train)
X_test = sc_X.transform(X_test)