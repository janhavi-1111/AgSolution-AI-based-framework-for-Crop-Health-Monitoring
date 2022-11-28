#!/usr/bin/env python
# coding: utf-8

# # Import Libraries

# In[1]:

import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn 
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.model_selection import train_test_split  
from sklearn.svm import SVC


# # Read the CSV file and Display data


dataset = pd.read_csv("crop_csv_file.csv")
dataset.head(10)


# # Describe the data

# In[4]:


dataset.describe()


# # Check the shape of data

# In[5]:


dataset.shape


# # Check NaN values

# In[6]:


dataset.isnull().sum()


# # Drop column

# In[7]:


df=dataset.drop(['Crop_Year'], axis = 1)


# # Check the shape

# In[8]:


df.shape


# # Drop missing values

# In[9]:


df=df.dropna()


# # Recheck if any missing value exist

# In[10]:


df.isnull().sum()


# # Checking the count of categories

# In[11]:


df['Season'].value_counts()


# In[12]:


df['Crop'].value_counts()


# In[13]:


df['District_Name'].value_counts()


# In[14]:


df['State_Name'].value_counts()


# # Label Encoding

# In[23]:


from sklearn import preprocessing
label_encoder=preprocessing.LabelEncoder()

State_Name=label_encoder.fit_transform(df.State_Name)
District_Name=label_encoder.fit_transform(df.District_Name)
Crop=label_encoder.fit_transform(df.Crop)
Season=label_encoder.fit_transform(df.Season)

df['State_Name']=State_Name
df['District_Name']=District_Name
df['Crop']=Crop
df['Season']=Season


# In[24]:


df


# # Define x and Y

# In[25]:


x= df.iloc[:,:-1] 

y = df.iloc[:,-1]


# # Test Train Split

# In[20]:


X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 100)


# # Build the Modles

# # Decision Tree Regressor

# In[22]:


from sklearn.tree import DecisionTreeRegressor
drm=DecisionTreeRegressor()
drm.fit(X_train, y_train)
y_pred = drm.predict(X_test)


# In[19]:


from sklearn.metrics import r2_score
r= r2_score(y_test,y_pred)
#print("R2score for DecisionTree Regressor  is",r )


# # Linear Regression

# In[ ]:


from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)


# In[ ]:


from sklearn.metrics import mean_squared_error,r2_score
mean_squared_error(y_test,y_pred)
r2_score(y_test,y_pred)


# # Random Forest Regressor

# In[ ]:


from sklearn.ensemble import RandomForestRegressor
rf=RandomForestRegressor(n_estimators=7,criterion='squared_error',random_state=0)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)


# In[ ]:


from sklearn.metrics import r2_score
r= r2_score(y_test,y_pred)
#print("R2score for RandomForest Regressor  is",r )


# # K Nearest Neighbours

# In[ ]:


from sklearn.neighbors import KNeighborsRegressor
classifier=KNeighborsRegressor(n_neighbors=1)
classifier.fit(x,y)
y_predict=classifier.predict(X_test)


# In[ ]:


from sklearn.metrics import r2_score
r= r2_score(y_test,y_predict)
#print("R2score for KNN Regressor  is",r )


# # Naive bayes

# In[ ]:


from sklearn.linear_model import BayesianRidge
br=BayesianRidge()
br.fit(x,y)
y_pred=br.predict(X_test)


# In[ ]:


from sklearn.metrics import r2_score
r= r2_score(y_test,y_predict)
#print("R2score for BayesianRidge Regressor  is",r )


# # Gradient Boosting Regressor

# In[ ]:


from sklearn.ensemble import GradientBoostingRegressor
gbr=GradientBoostingRegressor(n_estimators=50,max_depth=1,random_state=0)
gbr.fit(x,y)
y_pred=gbr.predict(X_test)


# In[ ]:


from sklearn.metrics import r2_score
r= r2_score(y_test,y_predict)
#print("R2score for Gradient Boosting Regressor  is",r )


# # XGboost Regressor

# In[ ]:


import xgboost as xg
xgb_r=xg.XGBRegressor(objective='reg:squarederror',n_estimators=10,seed=123)
xgb_r.fit(x,y)
y_pred=xgb_r.predict(X_test)


# In[ ]:


from sklearn.metrics import r2_score
r= r2_score(y_test,y_predict)
#print("R2score for Gradient Boosting Regressor  is",r )


# In[ ]:


classifier.predict([[1,5,3,40,37,40,46,1359.0]])


# In[ ]:

State = sys.argv[1]
District = sys.argv[1]
Season = sys.argv[1]
Crop = sys.argv[1]
Temperature = sys.argv[1]
Humidity = sys.argv[1]
Soilmoisture = sys.argv[1]
Area = sys.argv[1]
'''
State=input('Enter State:')
District=input('Enter District:')
Season=input('Enter Season:')
Crop=input('Enter Crop:')
Temperature=input('Enter Temperature:')
Humidity=input('Enter Humidity:')
Soilmoisture=input('Enter Soilmoisture:')
Area=input('Enter Area:')'''

Output=classifier.predict([[float(State),
                   float(District),
                   float(Season),
                   float(Crop),
                   float(Temperature),
                   float(Humidity),
                   float(Soilmoisture),
                   float(Area)]])
print(Output)
print('Crop Yeild Production:',Output)




