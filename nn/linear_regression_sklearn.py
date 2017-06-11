# Linear Regression with sklearn

# Imports

# %matplotlib inline
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import sklearn

# Dataset is included in sklearn

from sklearn.datasets import load_boston
boston = load_boston()
# boston is a dictionary object
boston.keys()
boston.data.shape
print(boston.feature_names)
print(boston.DESCR)
# check the data (without column name)
bos = pd.DataFrame(boston.data)
bos.head()

# add column name
bos.columns = boston.feature_names
bos.head()