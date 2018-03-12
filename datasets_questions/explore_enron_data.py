#!/usr/bin/python

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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print("Size of dataset")
print(len(enron_data))
print("Number of Features")
print(len(enron_data["SKILLING JEFFREY K"]))
print("The Features")
print(enron_data["SKILLING JEFFREY K"].keys())
count=0
for k in enron_data.keys():
	if enron_data[k]['poi']==1:
		count+=1
print("Number of POI")
print(count)
#print(enron_data.keys())
print('What is the total value of the stock belonging to James Prentice?')
print(enron_data["PRENTICE JAMES"]['total_stock_value'])
print('How many email messages do we have from Wesley Colwell to persons of interest?')
print(enron_data["COLWELL WESLEY"]['from_this_person_to_poi'])
print("What's the value of stock options exercised by Jeffrey K Skilling? ")
print(enron_data["SKILLING JEFFREY K"]['exercised_stock_options'])
print('People at the helm and their payments')
for k in ["SKILLING JEFFREY K","LAY KENNETH L","FASTOW ANDREW S"]:
    print(k,enron_data[k]['total_payments'])
print('Quantified Salary and Email Address')
salcount=emailcount=0
for k in enron_data.keys():
    if enron_data[k]['salary']!='NaN':
        salcount+=1
    if enron_data[k]['email_address']!='NaN':
        emailcount+=1
print('Quatified Salary: ',salcount)
print('Quantified Email Address: ',emailcount)