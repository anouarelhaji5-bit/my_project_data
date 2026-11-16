import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 
df = pd.read_csv("marketing_campaign.csv", sep="\t")
print(df)
print(df.head())
print(df.info())
print(df.shape)
print(df.isnull().sum())
df["Income"]=df ["Income"]. fillna(df ["Income"].median())
print(df["Income"])
print(df.isnull().sum())
print(df.duplicated())
print(df.duplicated().any())
print(df.dtypes)
for col in df.select_dtypes(include=["str"]).columns:
   if col != 'Dt_Customer':
     df[col] = df[col].str.strip().str.lower();
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], format='%d-%m-%Y')
print(df['Dt_Customer'].dtype)
df["Age"]= 2026 - df["Year_Birth"]
print(df["Age"].head())
tolal=["MntWines","MntFruits","MntMeatProducts","MntFishProducts","MntSweetProducts","MntGoldProds"]
df["Total_Spent"]=df[tolal].sum(axis=1)
df=df[df['Age']<=101]
df=df[df['Income']<=600000]
print(df.shape)
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Age', y='Total_Spent', alpha=0.6, color='purple')
plt.title('Age vs Total Spent', fontsize=14)
plt.xlabel('Age', fontsize=12)
plt.ylabel('Total Spent', fontsize=12)
plt.show()
sns.set_theme(style="whitegrid")
numeric_cols = (
    df.select_dtypes(include=['number']).drop(columns=['ID'], errors='ignore').columns)
for col in numeric_cols:
  plt.figure(figsize=(8, 5))
  sns.histplot(df[col], bins=15, color='teal', kde=True)
  plt.title(f' {col} (Distribution)', fontsize=12)
  plt.xlabel(col, fontsize=10)
  plt.ylabel('Count', fontsize=10)
  plt.show()
plt.figure(figsize=(10, 8))
corr_matrix = df.select_dtypes(include=['number']).corr()
sns.heatmap( corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap', fontsize=14)
plt.show()
for col in numeric_cols:
  plt.figure(figsize=(8, 4))
  sns.boxplot(x=df[col], color='orange')
  plt.title(f'Boxplot for {col}', fontsize=12)
  plt.xlabel(col, fontsize=10)
  plt.show()
df.to_csv('cleaned_data_marketing_campaign.csv', index=False)