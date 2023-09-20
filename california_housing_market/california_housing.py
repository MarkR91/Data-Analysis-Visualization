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


"""Try df = california_housing.fetch_california_housing()
calf_hous_df = pd.DataFrame(data= df.data, columns=df.feature_names)    
calf_hous_df.sample(4)"""

# Loading the dataset
# pd.set_option("display.max_rows", None)
# x = load_boston()
data = fetch_openml(name="house_prices", as_frame=True)
print("Attributes=", dir(data))

X = data.data
# print(X.columns)
# print(X.head(25))

print(X.shape)  # Check (rows, cols)
# print(X.info())  # Quick summary of df
# print(X.isnull().any())  # Check for null values
# print(type(X))
# for col, is_null in X.isnull().any().items():
#   print(col, is_null)
for attr in dir(data):
    print(attr, ":", getattr(data, attr))

# print(X.dtypes)  # Check data types

y = data.target  # Target variable
# print(y)

# for col in X.columns:
#   print(f"{col}: {X[col].isnull().any()}")

# for col in X.columns:
#    print(col, X[col].isnull().any())

# print(X.isnull().any()[X.isnull().any()].index)
# print(X[X.isnull().any()]) why this will not work to print the null values

"""
df = pd.DataFrame(x.data, columns=x.feature_names)  # Put data into dataframe
df["MEDV"] = x.target
X = df.drop("MEDV", 1)  # Feature matrix
y = df["MEDV"]  # Target variable
df.head()

# Using Pearson Correlation
plt.figure(figsize=(12, 10))
cor = df.corr()
sns.heatmap(cor, annot=True, cmap=plt.cm.Reds)
plt.show()

# Correlation with output variable
cor_target = abs(cor["MEDV"])  # Selecting highly correlated features
relevant_features = cor_target[cor_target > 0.5]
relevant_features
"""
