#!/usr/bin/env python
# coding: utf-8

# # Xgbfir simple example
# This is a small working example of Xgbfir usage from Python code.

# In[1]:

from sklearn.datasets import load_iris, load_boston
import xgboost as xgb
import xgbfir

# loading database
boston = load_boston()

# doing all the XGBoost magic
xgb_rmodel = xgb.XGBRegressor().fit(boston['data'], boston['target'])

# saving to file with proper feature names
xgbfir.saveXgbFI(xgb_rmodel, feature_names=boston.feature_names, OutputXlsxFile = 'bostonFI.xlsx')


# loading database
iris = load_iris()

# doing all the XGBoost magic
xgb_cmodel = xgb.XGBClassifier().fit(iris['data'], iris['target'])

# saving to file with proper feature names
xgbfir.saveXgbFI(xgb_cmodel, feature_names=iris.feature_names, OutputXlsxFile = 'irisFI.xlsx')


# Check working directory. There will be two new files: **bostonFI.xlsx** and **irisFI.xlsx**.
