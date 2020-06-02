# This is a summary of Pandas key elements

# The approach to learn Pandas quickly is as follows:
#    ***  Repeat the key elements by coding or writing on a paper every day for three days or more  ***

# This project uses the data from Kaggle: https://www.kaggle.com/c/m5-forecasting-accuracy/data
# You can download the 4 files from the website if you like. Two files have more than 100GB.

import pandas as pd

# import data
filepath = "C:\\User_name\\Kaggle\\"
a=pd.read_csv(filepath  + "sales_train_validation.csv")
c=pd.read_csv(filepath + "calendar.csv")

# the basic data structures are Series and DataFrame, you can create by yourself
onecol = pd.Series([1,2,3])
twocols = pd.DataFrame([1,2,3], [6,7,8])

# dataframe structure elements: index for rows, columns are just columns
a.describe() #for numerical variables, shows quantiles
c.columns
c.index

# the index is a special feature of pandas
test = a.copy() # make a copy of a, such that when you change test, a won't be changed
test.set_index('id') # column id becomes index, there is no id col afterwards
test['index'] = test.index # col index will be added after the last column

# show values in the data
a.iloc[1,2]
