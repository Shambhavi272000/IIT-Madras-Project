import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import r2_score
from math import sqrt
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV

from prettytable import PrettyTable

train_df = pd.read_excel("Data_Train.xlsx")
train_df.head(10)

train_df.columns

train_df.info()

train_df.describe()

train_df.isnull().head()

train_df.isnull().sum()

train_df.dropna(inplace = True)

train_df[train_df.duplicated()].head()

train_df.drop_duplicates(keep='first',inplace=True)
train_df.head()

train_df.shape

train_df["Additional_Info"].value_counts()

train_df["Airline"].unique()

train_df["Route"].unique()

test_df = pd.read_excel("Test_set.xlsx")
test_df.head(10)

test_df.columns

test_df.info()

test_df.describe()

test_df.isnull().sum()

sns.catplot(y = "Price", x = "Airline", data = train_df.sort_values("Price", ascending = False), kind="boxen", height = 8, aspect = 3)
plt.show()






