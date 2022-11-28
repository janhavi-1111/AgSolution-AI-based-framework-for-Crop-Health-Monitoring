#!/usr/bin/env python
# coding: utf-8

# # Import Libraries

# In[ ]:

import sys

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn 

from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier 
from sklearn.svm import SVC
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import VotingClassifier #bagging 
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import roc_curve,auc
import warnings
#warnings.filterwarnings(ignore)
#warnings.filterwarnings(action) 

#


# In[21]:

eval_metric='mlogloss'

dataset = pd.read_csv('crop_recommendation_pavan_khatal_farm.csv')
dataset.head(10)


# # Describe the data

# In[ ]:


dataset.describe()


# # Check the shape of data

# In[ ]:


dataset.shape


# # Check Nan Values

# In[ ]:


dataset.isnull().sum()


# # Label Encoding

# In[22]:

from sklearn import preprocessing
label_encoder=preprocessing.LabelEncoder()

label=label_encoder.fit_transform(dataset["vegetables/fruits"])

dataset['label']=label
dataset.drop(['vegetables/fruits'], axis=1,inplace=True)

# In[23]:


dataset


# # Define X and Y

# In[24]:


x= dataset.iloc[:,:-1] 

y = dataset.iloc[:,-1]


# # Train Test Split

# In[25]:


X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)


# # Standard Scaler

# In[26]:


from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
X_train=sc_X.fit_transform(X_train)
X_test=sc_X.fit_transform(X_test)


# # Build the Models

# # Decision tree

# In[27]:


cls = DecisionTreeClassifier(max_depth=10,splitter='best') 
cls.fit(X_train,y_train) #training of classifier
y_pred = cls.predict(X_test) 


# In[30]:


dt_acc=accuracy_score(y_test,y_pred)
dt_cls=classification_report(y_test, y_pred)


# # Random Forest

# In[31]:


rf = RandomForestClassifier(n_estimators=9,random_state=0)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)


# In[32]:


rf_acc=accuracy_score(y_test,y_pred)
rf_cls=classification_report(y_test, y_pred)


# # Support Vector Machine

# In[33]:


svm = SVC(probability=True,kernel = 'linear', random_state =1)
svm.fit(X_train, y_train)
y_pred = svm.predict(X_test)


# In[34]:


svm_acc=accuracy_score(y_test,y_pred)
svm_cls=classification_report(y_test, y_pred)


# # Bagging

# In[35]:


estimators = []
model1=  RandomForestClassifier()
estimators.append(('RandomForest', model1)) 
model2=  DecisionTreeClassifier()
estimators.append(('DecisionTree', model2)) 
model3 = SVC(probability=True)
estimators.append(('svm', model3))
ensemble = VotingClassifier(estimators,voting='soft') #bagging ensembLe 
eclf1 = ensemble.fit(X_train,y_train) 
y_pred=eclf1.predict(X_test)


# In[36]:


ens_acc=accuracy_score(y_test,y_pred)
ens_cls=classification_report(y_test, y_pred)


# # XGBoost

# In[37]:


ab = XGBClassifier()
ab.fit(X_train, y_train)
y_pred = ab.predict(X_test)


# In[38]:


xg_acc=accuracy_score(y_test,y_pred)
xg_cls=classification_report(y_test, y_pred)


# # Accuracy

# In[39]:


'''print("Accuracy for Decision Tree: ",dt_acc)
print("\n\n")

print("Accuracy for Random Forest: ",rf_acc)
print("\n\n")

print("Accuracy for SVM: ",svm_acc)
print("\n\n")

print("Accuracy for Bagging Method: ",ens_acc)
print("\n\n")

print("Accuracy for XGboost: ",xg_acc)


# # Classification Report

# In[40]:


print("Classification Report for Decision Tree: \n",dt_cls)
print("\n\n")

print("Classification Report for Random Forest: \n",rf_cls)
print("\n\n")

print("Classification Report for SVM:\n ",svm_cls)
print("\n\n")

print("Classification Report for Bagging Method: \n",ens_cls)
print("\n\n")

print("Classification Report for Xgboost: ",xg_cls)'''


# # Accuracy

# In[41]:


x=['Decision Tree','Random Forest','SVM','Bagging','Xgboost']
yacc=[dt_acc,rf_acc,svm_acc,ens_acc,xg_acc]


# In[42]:


data = {'Algorithms':x,
        'Accuracy':yacc,
        }


# In[43]:


df_acc=pd.DataFrame(data)
df_acc.head(5)


# In[44]:


df_acc.to_csv('Accuracy.csv',index=False)


# # Comparison of Accuracy

# In[45]:


labels = df_acc['Algorithms']
acc = df_acc['Accuracy']


x = np.arange(len(labels))  # the label locations
w = 0.6
dimw = w / 3
fig, ax = plt.subplots()
rects1 = ax.bar(x+1*dimw, acc, dimw, label='Accuracy')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by algorithms')
ax.set_xticks(x + dimw / 2)
ax.set_xticklabels(labels,rotation = 45)
ax.legend()

fig.tight_layout()

plt.show()


# # Prediction

# In[47]:

N = sys.argv[1]
P = sys.argv[1]
K = sys.argv[1]
Temperature = sys.argv[1]
Humidity = sys.argv[1]
pH = sys.argv[1]
'''N=input('Enter N:')
P=input('Enter P:')
K=input('Enter k:')
Temperature=input('Enter Temperature:')
Humidity=input('Enter Humidity:')
pH=input('Enter PH:')'''

Output=ensemble.predict([[
                   float(N),
                   float(P),
                   float(K),
                   float(Temperature),
                   float(Humidity),
                   float(pH)]])
print(Output)
print('Crop Predicted is :',Output)