"""Script based on article at https://towardsdatascience.com/feature-selection-with-pandas-e3690ad8504b"""
# importing libraries
# from sklearn.datasets import load_boston  # Boston dataset was deprecated .
from sklearn.datasets import fetch_openml
import pandas as pd

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# %matplotlib inline # Display plots inline in Jupyter notebook
from sklearn.model_selection import train_test_split  # Split data into train/test sets
from sklearn.linear_model import LinearRegression  # Linear regression model
from sklearn.feature_selection import RFE  # Feature selection method
from sklearn.linear_model import RidgeCV, LassoCV, Ridge, Lasso  # Regularization models


# Compare function
def compare_data(df, arr):
    print(df.shape == arr.shape)
    print(list(df.columns) == data.feature_names)
    print(df.equals(pd.DataFrame(arr, columns=data.feature_names)))


# Loading the dataset
pd.set_option("display.max_rows", None)

data = fetch_openml(name="house_prices", as_frame=True)
# print("Attributes=", dir(data))
print(data.keys())

X = data.frame
# X = data.frame.values  # convert data.frame to numpy array
B = data.data

# compare_data(X, B)

# B_np = np.array(B)
print("columns in X ==>", X.columns)
# print(B.columns)

# drop columns with non-numerical data in them
"""
del X["Id"]  # Drop "Id" without resetting index?
del X["MSZoning"]
del X["Street"]
del X["Alley"]
del X["MiscFeature"]
del X["SaleType"]
del X["SaleCondition"]
del X["LotShape"]
del X["LandContour"]
del X["Utilities"]
del X["LotConfig"]
del X["PoolQC"]
del X["Fence"]
del X["LandSlope"]
del X["Neighborhood"]
del X["Condition1"]
"""
print(X.info())
non_numeric_cols = X.select_dtypes("object")
X = X.drop(non_numeric_cols, axis=1)


print(X.head(25))
print(X.info())
# print(B.head(25))

print("X=", type(X))
# print("B=", type(B))


# print(X.shape)  # Check (rows, cols)
# print(X.info())  # Quick summary of df
# print(X.isnull().any())  # Check for null values
# print(type(X))
# for col, is_null in X.isnull().any().items():
#   print(col, is_null)
# for attr in dir(data):
#   print(attr, ":", getattr(data, attr))

# print(X.dtypes)  # Check data types

y = data.target  # Target variable
# print(y.head(10))
# print(y.tail(10))

# for col in X.columns:
#   print(f"{col}: {X[col].isnull().any()}")

# for col in X.columns:
#    print(col, X[col].isnull().any())

# print(X.isnull().any()[X.isnull().any()].index)
# print(X[X.isnull().any()]) why this will not work to print the null values






