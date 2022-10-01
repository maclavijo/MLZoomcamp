#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display
import seaborn as sns
from sklearn import set_config
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn import model_selection
set_config(display='diagram')

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# Read the data
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
df.head()


# #### Peparing and cleaning data

# In[3]:


# Standarize data formats
df.columns = df.columns.str.lower().str.replace(' ','_')
categCols = df.select_dtypes('object').columns.to_list()

for col in categCols:
    df[col] = df[col].str.lower().str.replace(' ','_')
df.head()


# In[4]:


# Correct values and type of variable totalcharges

df.totalcharges = pd.to_numeric(df.totalcharges, errors='coerce')

# Characters that couldn't be converted to numerical values show as nan
print(f'Null values for column totalcharges: {df.totalcharges.isnull().sum()}')

# Filling missing values with zero
df.totalcharges.fillna(0, inplace=True)
print(f'Null values for column totalcharges after converting to numerical and fillin NAs: {df.totalcharges.isnull().sum()}')


# In[5]:


# Make seniorcitizen an object type variable
#df.seniorcitizen = df.seniorcitizen.astype(bool).astype(object)


# In[6]:


df.head().T


# In[7]:


rows = []
for col in df.columns:
    rows.append([col,df[col].dtype, df[col].unique()]) 
pd.DataFrame(rows, columns=['Feature', 'Type', 'Unique Values'])


# In[8]:


targetCol = 'churn'
target = df[targetCol]
data = df.drop(columns=[targetCol])


# In[9]:


# Getting numerical and categorical columns

from sklearn.compose import make_column_selector as selector

numColSelector = selector(dtype_exclude=object)
ctgColSelector = selector(dtype_include=object)

numericalCols = numColSelector(data)
categoricalCols = ctgColSelector(data)

del numericalCols[0]
categoricalCols.insert(1, 'seniorcitizen')
del categoricalCols[0]


# In[10]:


print(numericalCols)
print(categoricalCols)


# In[11]:


# creating preprocesors

from sklearn.preprocessing import OneHotEncoder, StandardScaler

catPreprocessor = OneHotEncoder(handle_unknown="ignore")
numPreprocessor = StandardScaler()


# In[12]:


# Transforming the data

from sklearn.compose import ColumnTransformer

preprocessor = ColumnTransformer([
    ('one-hot-encoder', catPreprocessor, categoricalCols)],remainder="passthrough")
    #('one-hot-encoder', catPreprocessor, categoricalCols),
    #('standard_scaler', numPreprocessor, numericalCols)])


# In[90]:


# creating the model

from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline, Pipeline

model = make_pipeline(preprocessor, LogisticRegression(max_iter=1000))


# In[91]:


# Splitting the data

from sklearn.model_selection import train_test_split,cross_val_predict

allColumns = numericalCols + categoricalCols
dataTrainFull, dataTest, targetTrainFull, targetTest = train_test_split(
    data[allColumns], target, test_size=0.2, random_state=1)

dataTrain, dataVal, targetTrain, targetVal = train_test_split(
    dataTrainFull, targetTrainFull, test_size=0.25, random_state=1)

print(len(dataTrain), len(dataVal), len(dataTest))


# In[92]:


_ = model.fit(dataTrain, targetTrain)
display(targetVal[:5].values)
display(model.score(dataVal, targetVal))


# In[93]:


# Let's use the train full dataset and calculate AUC
from sklearn.metrics import auc, roc_auc_score

_ = model.fit(dataTrainFull, targetTrainFull)
targetPred = model.predict_proba(dataTest)[:,1]

auc = roc_auc_score(targetTest, targetPred)
auc


# In[94]:


# Test user # 1
user = dataVal.iloc[280].to_dict()
user


# In[95]:


u = pd.DataFrame(user, index=[1])
model.predict_proba(u)[0][1]


# In[96]:


# List of users to test
users = dataVal.iloc[100:120].to_dict('records')
users


# In[97]:


# Testing user by user 
ypred = []
for u in users:
    x = pd.DataFrame(u, index=[1])
    res = model.predict_proba(x)[0][1]
    ypred.append(res)
np.array(ypred)


# In[98]:


# converting list of dicts in dataframe
us = pd.DataFrame(users)
ypred = model.predict_proba(us)
ypred[:,1]


# In[99]:


from sklearn.model_selection import cross_validate, cross_val_score

cv_results = cross_val_score(model, dataTrainFull, targetTrainFull, scoring='roc_auc', cv=5)
cv_results


# In[100]:


print("The mean cross-validation accuracy is: "
      f"{cv_results.mean():.3f} +/- {cv_results.std():.3f}")


# #### Use pickle to save the model

# In[101]:


import pickle
C = 1
outputFile = f'model_C={C}.bin'
outputFile


# In[102]:


with open(outputFile, 'wb') as f:
    pickle.dump(model, f)


# #### Load the model

# In[103]:


clear model


# In[104]:


modelFile = 'model_C=1.0.bin'
with open(outputFile, 'rb') as f:
    newModel = pickle.load(f)
    


# In[105]:


newModel


# In[112]:


# Test user
user = dataVal.iloc[1].to_dict()
user


# In[114]:


u = pd.DataFrame(user, index=[1])
newModel.predict_proba(u)[0][1]


# In[ ]:




