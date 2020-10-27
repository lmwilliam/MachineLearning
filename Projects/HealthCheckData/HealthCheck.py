# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 20:54:01 2020

@author: WilliamLiang
"""

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

# Load Dataset
dataset = pd.read_csv("HealthCheck.csv")

# Spliting dataset into Independent Variable & Dependent Variable
IV = dataset.iloc[:, :-1].values
DV = dataset.iloc[:, -1].values

# Missing data imputing (use "mean" strategy)
imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
imputer = imputer.fit(IV[:, 1:4])
IV[:, 1:4] = imputer.transform(IV[:, 1:4])

# Turn no/yes into 0, 1
labelEncoder = LabelEncoder()
# Make sure value is a float number
DV = labelEncoder.fit_transform(DV).astype("float64")

# Turn multivalue into 0, 1
dummies = pd.get_dummies(IV[:,0]).values
IV = np.concatenate((dummies, IV[:,1:4]), axis = 1).astype("float64")

# Spliting dataset into training and testing dataset
IV_train,IV_test,DV_train,DV_test = train_test_split(IV, DV, test_size = 0.2, random_state = 0)

# Feature scaling
scaler_IV = StandardScaler().fit(IV_train)
IV_train = scaler_IV.transform(IV_train)
IV_test = scaler_IV.transform(IV_test)

# Print the feature scaling result
print("Independent variable training dataset:", "\n", IV_train, "\n")
print("Dependent variable training dataset:", "\n", DV_train, "\n")
print("Independent variable testing dataset:", "\n", IV_test, "\n")
print("Dependent variable testing dataset:", "\n", DV_test, "\n")
