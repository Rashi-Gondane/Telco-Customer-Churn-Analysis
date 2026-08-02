import pandas as pd

df=pd.read_csv("C:/Users/rashi/Downloads/archive (4)/WA_Fn-UseC_-Telco-Customer-Churn.csv")
print(df)

#checking non-null values as well as data types getting overall view
print(df.info())

#changing the data type of TotalCharge (this will convert any non-numeric value ,  or blank with string to NaN)
df['TotalCharges']=pd.to_numeric(df['TotalCharges'] , errors='coerce')
print(df.dtypes)

# filling NaN with zero
df['TotalCharges']=df['TotalCharges'].fillna(0)
# checking that did the TotalCharges column have any null values left
print(df.isnull().sum())

# checking duplicates values
print(df.duplicated().sum())
print(df.duplicated('customerID').sum())

# Saving csv
df.to_csv( "C:/Users/rashi/Downloads/telco_cleaned.csv",  index=False)
print('CSV loaded successfully')

# Summary statistics
print(df.describe())

# gender wise churn rate
df1=(df['Churn']== 'Yes').groupby(df['gender']).mean()*100
print(df1)
# Citizen wise churn rate
df2=(df['Churn']== 'Yes').groupby(df['SeniorCitizen']).mean()*100
print(df2)
# Dependents wise churn rate
df3=(df['Churn']== 'Yes').groupby(df['Dependents']).mean()*100
print(df3)
# SeniorCitizen who got churned were they dependent or not
df4=((df['Dependents']== 'Yes') & (df['Churn']=='Yes')).groupby(df['SeniorCitizen']).mean()*100
print(df4)
# partner wise churn rate
df5=(df['Churn'] == 'Yes').groupby(df['Partner']== 'Yes').mean()*100
print(df5)
# PhoneService wise churn rate
df6=(df['Churn'] == 'Yes').groupby(df['PhoneService']).mean()*100
print(df6)
# MultipleLines wise churn rate
df7=(df['Churn'] == 'Yes').groupby(df['MultipleLines']).mean()*100
print(df7)
# Internet Service wise churn rate
df8=(df['Churn'] == 'Yes').groupby(df['InternetService']).mean()*100
print(df8)
# OnlineSecurity wise churn rate
df9=(df['Churn'] == 'Yes').groupby(df['OnlineSecurity']).mean()*100
print(df9)
# OnlineBackup wise churn rate
df10=(df['Churn'] == 'Yes').groupby(df['OnlineBackup']).mean()*100
print(df10)
# DeviceProtection wise churn rate
df11=(df['Churn'] == 'Yes').groupby(df['DeviceProtection']).mean()*100
print(df11)
# TechSupport wise churn rate
df12=(df['Churn'] == 'Yes').groupby(df['TechSupport']).mean()*100
print(df12)
# StreamingTV wise churn rate
df13=(df['Churn'] == 'Yes').groupby(df['StreamingTV']).mean()*100
print(df13)
# StreamingMovies wise churn rate
df14=(df['Churn'] == 'Yes').groupby(df['StreamingMovies']).mean()*100
print(df14)
# Contract wise churn rate
df15=(df['Churn'] == 'Yes').groupby(df['Contract']).mean()*100
print(df15)
# PaperlessBilling wise churn rate
df16=(df['Churn'] == 'Yes').groupby(df['PaperlessBilling']).mean()*100
print(df16)
# PaymentMethod wise churn rate
df17=(df['Churn'] == 'Yes').groupby(df['PaymentMethod']).mean()*100
print(df17)
# Monthly charges
df18=df[
    (df['PhoneService']=='Yes') &
    (df['MultipleLines']=='No') &
    (df['OnlineBackup']=='No') &
    (df['OnlineSecurity']=='No') &
    (df['DeviceProtection']=='No') &
    (df['TechSupport']=='No') &
    (df['StreamingTV']=='No') &
    (df['StreamingMovies']=='No') &
    (df['Contract']=='Month-to-month')
]
print(df18[['InternetService' , 'MonthlyCharges']])



















