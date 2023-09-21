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


# Loading the dataset
pd.set_option("display.max_rows", None)

data = fetch_openml(name="house_prices", as_frame=True)
# print("Attributes=", dir(data))
# print(data.keys())

X = data.frame
# X = data.frame.values  # convert data.frame to numpy array

B = data.data.to_numpy()

# B_np = np.array(B)
# print(X.columns)
# print(B.columns)
print(X.head(25))
print(B[0:25])

print("X=", type(X))
print("B=", type(B))


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
print(y.head(10))
print(y.tail(10))

# for col in X.columns:
#   print(f"{col}: {X[col].isnull().any()}")

# for col in X.columns:
#    print(col, X[col].isnull().any())

# print(X.isnull().any()[X.isnull().any()].index)
# print(X[X.isnull().any()]) why this will not work to print the null values
