#!/usr/bin/env python
# coding: utf-8

# # Import Libraries

# In[57]:


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


# # Read the csv file and display it

# In[58]:


dataset = pd.read_csv("data.csv")
dataset.head(10)


# # Describe the data

# In[59]:


dataset.describe()


# # Check the shape of data

# In[60]:


dataset.shape


# # Check nan values

# In[61]:


dataset.isnull().sum()


# # Label Encoding

# In[62]:


from sklearn import preprocessing
label_encoder=preprocessing.LabelEncoder()

Output=label_encoder.fit_transform(dataset.Output)

dataset['Output']=Output


# In[63]:


dataset.head()


# # Define X and Y

# In[64]:


x= dataset.iloc[:,:-1] 

y = dataset.iloc[:,-1]


# # Test Train Split

# In[65]:


X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 100)


# # Standard Scaler

# In[66]:


from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
X_train=sc_X.fit_transform(X_train)
X_test=sc_X.fit_transform(X_test)


# # Build the Models

# # Decision Tree

# In[67]:


cls = DecisionTreeClassifier() 
cls.fit(X_train,y_train) #training of classifier
y_pred = cls.predict(X_test) 
y_pred_prob_dt = cls.predict_proba(X_test)[:,1]
fpr_dt, tpr_dt, thresholds_dt = roc_curve(y_test, y_pred_prob_dt)
roc_auc_dt = auc(fpr_dt, tpr_dt)


# In[68]:


dt_acc=accuracy_score(y_test,y_pred)
dt_cls=classification_report(y_test, y_pred)


# In[69]:


conf_matrix = confusion_matrix(y_pred,y_test)
print(conf_matrix)


# # Random Forest

# In[70]:


rf = RandomForestClassifier()
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
y_pred_prob_rf = rf.predict_proba(X_test)[:,1]
fpr_rf, tpr_rf, thresholds_rf = roc_curve(y_test, y_pred_prob_rf)
roc_auc_rf = auc(fpr_rf, tpr_rf)


# In[71]:


rf_acc=accuracy_score(y_test,y_pred)
rf_cls=classification_report(y_test, y_pred)


# # Support Vector Machine

# In[72]:


svm = SVC(probability=True,kernel = 'rbf', random_state =3)
svm.fit(X_train, y_train)
y_pred = svm.predict(X_test)
y_pred_prob_svm = svm.predict_proba(X_test)[:,1]
fpr_svm, tpr_svm, thresholds_svm = roc_curve(y_test, y_pred_prob_svm)
roc_auc_svm = auc(fpr_svm, tpr_svm)


# In[73]:


svm_acc=accuracy_score(y_test,y_pred)
svm_cls=classification_report(y_test, y_pred)


# # Bagging

# In[74]:


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
y_pred_prob_en = ensemble.predict_proba(X_test)[:,1]
fpr_en, tpr_en, thresholds_en = roc_curve(y_test, y_pred_prob_en)
roc_auc_en = auc(fpr_en, tpr_en)


# In[75]:


ens_acc=accuracy_score(y_test,y_pred)
ens_cls=classification_report(y_test, y_pred)


# # XGBoost

# In[76]:


ab = XGBClassifier()
ab.fit(X_train, y_train)
y_pred = ab.predict(X_test)
y_pred_prob_xg = ab.predict_proba(X_test)[:,1]
fpr_xg, tpr_xg, thresholds_xg = roc_curve(y_test, y_pred_prob_xg)
roc_auc_xg = auc(fpr_xg, tpr_xg)


# In[77]:


xg_acc=accuracy_score(y_test,y_pred)
xg_cls=classification_report(y_test, y_pred)


# # Printing the Accuracy 

# In[78]:

'''
print("Accuracy for Decision Tree: ",dt_acc)
print("\n\n")

print("Accuracy for Random Forest: ",rf_acc)
print("\n\n")

print("Accuracy for SVM: ",svm_acc)
print("\n\n")

print("Accuracy for Bagging Method: ",ens_acc)
print("\n\n")

print("Accuracy for XGboost: ",xg_acc)


# # Print classification report

# In[79]:


print("Classification Report for Decision Tree: \n",dt_cls)
print("\n\n")

print("Classification Report for Random Forest: \n",rf_cls)
print("\n\n")

print("Classification Report for SVM:\n ",svm_cls)
print("\n\n")

print("Classification Report for Bagging Method: \n",ens_cls)
print("\n\n")

print("Classification Report for Xgboost: ",xg_cls)


# # ROC Curve
'''
# In[80]:


plt.plot([0, 1], [0, 1], 'k--')
plt.plot(fpr_dt, tpr_dt, label='Decision Tree (area = %0.3f)' % roc_auc_dt)
plt.plot(fpr_rf, tpr_rf, label='Random Forest (area = %0.3f)' % roc_auc_rf)
plt.plot(fpr_svm, tpr_svm, label='SVM (area = %0.3f)' % roc_auc_svm)
plt.plot(fpr_en, tpr_en, label='Ensemble (area = %0.3f)' % roc_auc_en)
plt.plot(fpr_xg, tpr_xg, label='Xgboost (area = %0.3f)' % roc_auc_xg)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC curves from the investigated models')
plt.legend(loc='best')
plt.show()


# # Saving the accuracy in dataframe

# In[81]:


x=['Decision Tree','Random Forest','SVM','Bagging','Xgboost']
yacc=[dt_acc,rf_acc,svm_acc,ens_acc,xg_acc]


# In[82]:


data = {'Algorithms':x,
        'Accuracy':yacc,
        }


# In[83]:


df_acc=pd.DataFrame(data)
df_acc.head(5)


# In[84]:


df_acc.to_csv('Accuracy.csv',index=False)


# # Comparison of Accuracy for each model using bar graph

# In[85]:


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

# In[95]:


pH= sys.argv[1]
EC= sys.argv[1]
OC= sys.argv[1]
OM= sys.argv[1]
N= sys.argv[1]
P= sys.argv[1]
K= sys.argv[1]
Zn= sys.argv[1]
Fe= sys.argv[1]
Cu= sys.argv[1]
Mn= sys.argv[1]
Sand= sys.argv[1]
Silt= sys.argv[1]
Clay= sys.argv[1]
CaCO3= sys.argv[1]
CEC= sys.argv[1]
Output=ensemble.predict([[float(pH),
                   float(EC),
                   float(OC),
                   float(OM),
                   float(N),
                   float(P),
                   float(K),
                   float(Zn),
                   float(Fe),
                   float(Cu),
                   float(Mn),
                   float(Sand),
                   float(Silt),
                   float(Clay),
                   float(CaCO3),
                   float(CEC),]])
print(Output)
print('Fertility Production:',Output)


# In[ ]:




