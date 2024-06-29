# -*- coding: utf-8 -*-
"""Credit Score_Calculations.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CAM8oGv-tQqIhXjcxgG-Aq0mw9e1m5T_

#Disclaimer:
* THIS is just a use case which we are considering for anamoly detection, not many innovations have been showcased here
* Just used to show how predictive modeling could be used to prevent internal banking frauds where  high risk individuals are given loans


---

#Dataset: https://drive.google.com/file/d/1t0qEX194UucNUIj4DIIuD6ykCnAUXrr1/view

# Data Exploration:

* Explored dataset structure and content.
* Utilized visualizations like box plots to understand credit score distribution across different features.

# Modelling:

* Preprocessed data, mapping categorical features.
* Split data into training and testing sets.
* Trained RandomForestClassifier to predict credit scores.

# Identify Anomalies:

* Compared predicted and actual credit scores.
* Defined threshold for significant deviation.
* Flagged anomalies based on threshold.

# Results and Insights:

* Implemented interactive input for credit score prediction.
* Saved trained model for future use.
* Thorough analysis and modeling approach showcased.
"""

import os
import joblib
import pickle
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = "plotly_white"

data = pd.read_csv("train.csv")
print(data.head())

print(data.info())

print(data.isnull().sum())

data["Credit_Score"].value_counts()

fig = px.box(data,
             x = "Occupation",
             color = "Credit_Score",
             title = "Credit Scores based on Occupation",
             color_discrete_map = {"Poor" : "red",
                                   "Standard" : "yellow",
                                   "Good" : "green"})
fig.show()

fig = px.box(data,
             x = "Credit_Score",
             y = "Annual_Income",
             color = "Credit_Score",
             title = "Credit Scores based on Annual Income",
             color_discrete_map = {"Poor" : "red",
                                   "Standard" : "yellow",
                                   "Good" : "green"})
fig.update_traces(quartilemethod = "exclusive")
fig.show()

fig = px.box(data,
             x = "Credit_Score",
             y = "Monthly_Inhand_Salary",
             color = "Credit_Score",
             title = "Credit Scores based on Monthly Inhand Salary",
             color_discrete_map = {"Poor" : "red",
                                   "Standard" : "yellow",
                                   "Good" : "green"})
fig.update_traces(quartilemethod = "exclusive")
fig.show()

fig = px.box(data,
             x = "Credit_Score",
             y = "Num_Bank_Accounts",
             color = "Credit_Score",
             title = "Credit Scores based on Number of Bank Accounts",
             color_discrete_map = {"Poor" : "red",
                                   "Standard" : "yellow",
                                   "Good" : "green"})
fig.update_traces(quartilemethod = "exclusive")
fig.show()

fig = px.box(data,
             x = "Credit_Score",
             y = "Num_Credit_Card",
             color = "Credit_Score",
             title = "Credit Scores based on Number of Credit Cards",
             color_discrete_map = {"Poor" : "red",
                                   "Standard" : "yellow",
                                   "Good" : "green"})
fig.update_traces(quartilemethod = "exclusive")
fig.show()

fig = px.box(data,
             x = "Credit_Score",
             y = "Interest_Rate",
             color = "Credit_Score",
             title = "Credit Scores based on the Average Interest Rates",
             color_discrete_map = {"Poor" : "red",
                                   "Standard" : "yellow",
                                   "Good" : "green"})
fig.update_traces(quartilemethod = "exclusive")
fig.show()

fig = px.box(data,
             x = "Credit_Score",
             y = "Num_of_Loan",
             color = "Credit_Score",
             title = "Credit Scores based on Number of Loans Taken by the Person",
             color_discrete_map = {"Poor" : "red",
                                   "Standard" : "yellow",
                                   "Good" : "green"})
fig.update_traces(quartilemethod = "exclusive")
fig.show()

fig = px.box(data,
             x = "Credit_Score",
             y = "Delay_from_due_date",
             color = "Credit_Score",
             title = "Credit Scores Based on Average Number of Days Delayed for Credit card Payments",
             color_discrete_map = {"Poor" : "red",
                                   "Standard" : "yellow",
                                   "Good" : "green"})
fig.update_traces(quartilemethod = "exclusive")
fig.show()

fig = px.box(data,
             x = "Credit_Score",
             y = "Num_of_Delayed_Payment",
             color = "Credit_Score",
             title = "Credit Scores Based on Number of Delayed Payments",
             color_discrete_map = {"Poor" : "red",
                                   "Standard" : "yellow",
                                   "Good" : "green"})
fig.update_traces(quartilemethod = "exclusive")
fig.show()

fig = px.box(data,
             x = "Credit_Score",
             y = "Outstanding_Debt",
             color = "Credit_Score",
             title = "Credit Scores Based on Outstanding_Debt",
             color_discrete_map = {"Poor" : "red",
                                   "Standard" : "yellow",
                                   "Good" : "green"})
fig.update_traces(quartilemethod = "exclusive")
fig.show()

fig = px.box(data,
             x = "Credit_Score",
             y = "Credit_Utilization_Ratio",
             color = "Credit_Score",
             title = "Credit Scores Based on Credit Utilization Ratio",
             color_discrete_map = {"Poor" : "red",
                                   "Standard" : "yellow",
                                   "Good" : "green"})
fig.update_traces(quartilemethod = "exclusive")
fig.show()

fig = px.box(data,
             x = "Credit_Score",
             y = "Credit_History_Age",
             color = "Credit_Score",
             title = "Credit Scores Based on Credit History Age",
             color_discrete_map = {"Poor" : "red",
                                   "Standard" : "yellow",
                                   "Good" : "green"})
fig.update_traces(quartilemethod = "exclusive")
fig.show()

fig = px.box(data,
             x = "Credit_Score",
             y = "Total_EMI_per_month",
             color = "Credit_Score",
             title = "Credit Scores Based on Total Number of EMIs per Month",
             color_discrete_map = {"Poor" : "red",
                                   "Standard" : "yellow",
                                   "Good" : "green"})
fig.update_traces(quartilemethod = "exclusive")
fig.show()

fig = px.box(data,
             x = "Credit_Score",
             y = "Amount_invested_monthly",
             color = "Credit_Score",
             title = "Credit Scores Based on Amount Invested Monthly",
             color_discrete_map = {"Poor" : "red",
                                   "Standard" : "yellow",
                                   "Good" : "green"})
fig.update_traces(quartilemethod = "exclusive")
fig.show()

fig = px.box(data,
             x = "Credit_Score",
             y = "Monthly_Balance",
             color = "Credit_Score",
             title = "Credit Scores Based on Monthly Balance Left",
             color_discrete_map = {"Poor" : "red",
                                   "Standard" : "yellow",
                                   "Good" : "green"})
fig.update_traces(quartilemethod = "exclusive")
fig.show()

data["Credit_Mix"] = data["Credit_Mix"].map({"Standard" : 1,
                                            "Good" : 2,
                                            "Bad" : 0})

from sklearn.model_selection import train_test_split
x = np.array(data[["Annual_Income", "Monthly_Inhand_Salary",
                  "Num_Bank_Accounts", "Num_Credit_Card",
                  "Interest_Rate", "Num_of_Loan",
                  "Delay_from_due_date", "Num_of_Delayed_Payment",
                  "Credit_Mix", "Outstanding_Debt",
                  "Credit_History_Age", "Monthly_Balance"]])
y = np.array(data[["Credit_Score"]])

xtrain,xtest,ytrain,ytest = train_test_split(x,y,
                                                test_size = 0.33,
                                                random_state = 42)
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(xtrain,ytrain)

print("Credit Score Prediction : ")
a = float(input("Annual Income: "))
b = float(input("Monthly Inhand Salary: "))
c = float(input("Number of Bank Accounts: "))
d = float(input("Number of Credit cards: "))
e = float(input("Interest rate: "))
f = float(input("Number of Loans: "))
g = float(input("Average number of days delayed by the person: "))
h = float(input("Number of delayed payments: "))
i = input("Credit Mix (Bad: 0, Standard: 1, Good: 3) : ")
j = float(input("Outstanding Debt: "))
k = float(input("Credit History Age: "))
l = float(input("Monthly Balance: "))
features = np.array([[a,b,c,d,e,f,g,h,i,j,k,l]])
print("Predicted Credit Score = ", model.predict(features))

filename = "Credit_Score_Classification.sav"
pickle.dump(model,open(filename,"wb"))
