#!/usr/bin/python
# -*- coding: utf-8 -*-

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import pandas as pd

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
df = pd.DataFrame(enron_data).transpose()

# number of data points as True
df.poi.value_counts()[True]

# total value of the stock belonging to James Prentice
df.transpose()["PRENTICE JAMES"]

# number of email messages from Wesley Colwell to persons of interest
df.transpose()["COLWELL WESLEY"]

# value of stock options exercised by Jeffrey K Skilling
df.transpose()["SKILLING JEFFREY K"]

# Enron's CEO during much of the time fraud was ongoin
df.transpose()["SKILLING JEFFREY K"]

# chairman of the Enron board of directors
df.transpose()['LAY KENNETH L']

# CFO (chief financial officer) of Enron during most of the time that fraud was going on
df.transpose()['FASTOW ANDREW S']

# Of these three individuals (Lay, Skilling and Fastow), who took home the most money (largest value of “total_payments” feature)
skilling = ("Skilling", df.transpose()["SKILLING JEFFREY K"]["total_payments"])
lay = ("Lay", df.transpose()["LAY KENNETH L"]["total_payments"])
fastow = ("Fastow", df.transpose()["FASTOW ANDREW S"]["total_payments"])

heads = [skilling, lay, fastow]

def getKey(item):
    return item[1]

sorted(heads, key=getKey, reverse=True)

# How many folks in this dataset have a quantified salary? What about a known email address?
# salary
len(df)-df.salary.value_counts()['NaN']
# email address
len(df)-df.email_address.value_counts()['NaN']

# How many people in the E+F dataset (as it currently exists) have “NaN” for their total payments? What percentage of people in the dataset as a whole is this?
# number of people
df.total_payments.value_counts()['NaN']
# percentage of total
float(df.total_payments.value_counts()['NaN'])/len(df)*100

# How many POIs in the E+F dataset have “NaN” for their total payments? What percentage of POI’s as a whole is this?
df.where(df.poi == True).total_payments.value_counts()

# If you added in, say, 10 more data points which were all POI’s, and put “NaN” for the total payments for those folks, the numbers you just calculated would change.
# What is the new number of people of the dataset? What is the new number of folks with “NaN” for total payments?
# new number of people of the dataset
len(df) + 10
# new number of folks with “NaN” for total payments
df.total_payments.value_counts()['NaN'] + 10

# What is the new number of POI’s in the dataset? 
df.poi.value_counts()[True] + 10
#What is the new number of POI’s with NaN for total_payments?
df.where(df.poi == True).total_payments.value_counts()



