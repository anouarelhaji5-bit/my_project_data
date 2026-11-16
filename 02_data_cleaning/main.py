import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np 
df=pd.read_csv("customer_churn_prediction_dataset.csv")
print(df)
print(df.info())
print(df.isnull().sum())
for col in df.columns:
   if df[col].nunique() < 10:
      print(f"{col} : {df[col].unique()}");
print(df.duplicated().sum())
df = df.drop('customerID', axis=1)
print(df)
print(df.describe())
df1 = df.replace({'No internet service': 'No', 'No phone service': 'No'})
print(df1)
sns.countplot(x='Churn', data=df1)
plt.title('Distribution of Customer Churn')
plt.xlabel('Churn')
plt.ylabel('Number of Customers')
plt.show()
df.to_csv('cleaned_data_customer_churn_prediction_dataset.csv', index=False)