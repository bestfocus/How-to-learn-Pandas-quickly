# This is a summary of Pandas key elements

# The approach to learn Pandas quickly is as follows:
#    ***  Repeat the key elements by coding or writing on a paper every day for three days or more  ***

# This project uses the data from Kaggle: https://www.kaggle.com/c/m5-forecasting-accuracy/data
# You can download the 4 files from the website if you like. Two files have more than 100GB.

import pandas as pd

# import data and generate DataFrame a and c
filepath = "C:\\User_name\\Kaggle\\"
a=pd.read_csv(filepath  + "sales_train_validation.csv")
c=pd.read_csv(filepath + "calendar.csv")

# the basic data structures are Series and DataFrame, you can create by yourself
onecol = pd.Series([1,2,3])
twocols = pd.DataFrame([1,2,3], [6,7,8])

# dataframe structure elements: 1. index for rows, 2. columns are just columns
a.describe() #for numerical variables, shows quantiles
a.head() # show top 10 rows of the data
c.columns
c.index
c.dtypes

# the index is a special feature of pandas
test = a.copy() # make a copy of a, such that when you change test, a won't be changed
test.set_index('id') # column id becomes index, there is no id col afterwards
test['index'] = test.index # col index will be added after the last column

# show values in the data
a.iloc[1,2] # this uses the matrix positions of the elements, first is row position, second is column position, index starts from 0
a.loc[:, 'id'] # ':' means including all
# find items by using condition
a[a['item_id']=='HOBBIES_1_001']
test.where(test['cat_id']=='FOODS') #show False results as NaN too
a[a['cat_id'].isin(['HOBBIES', 'FOODS'])] # isin select the items containing cat_id in the list

# Change the data
# add new columns
test['type']=test['id'].apply(lambda x: x[-10:])
test[test['type']=='validation']
# use sort_values to order the data by a column name
test = test.sort_values('id')
#rearrange the order of the columns
cols = test.columns.tolist()
test = test[[cols[-1]] + cols[:-1]]

# select top 10 smallest
dailymean=a[6:].mean()
c[c['d'].isin(dailymean.sort_values()[:10].index)]

# join
pd.merge(a, test[test['type']=='validation']) # merge by id, keep the same index
b.iloc[:30490, :1].join(a.iloc[:,1:]) # index are the same, there are no overlap columns
b.iloc[:30490, :1].merge(a, how='inner', left_on='id', right_on='id') # if orders of id are different in b and a, merge and use b's order

# find the intersection of two results
set(c['event_name_1'].unique()).intersection(c['event_name_2'].unique())

# delete
index1 = test[test['item_id']=='HOBBIES_1_001'].index
test.drop(index1, inplace=True) # delete rows
del test['type'] # delete a column

# aggregate by a group
a.iloc[:, 6:].mean(axis=1) # mean for each row
a.groupby('cat_id').sum()
# these are the same
a.groupby('cat_id').size()
a['cat_id'].value_counts()
a.groupby('state_id').mean().mean(axis=1)
test[12:20].sum(axis=0)

# TO BE CONTINUED ...

