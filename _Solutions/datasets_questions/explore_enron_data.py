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
d = enron_data
#Count no of features available in dataset.
#print enron_data
#print len(enron_data.values()[0])

#Count how many number of poi's values are as true
#count = 0

# for i in d.values():
# 	if(i["poi"] == True):
# 		count+=1

# print count

#How many POIs are there in total?
# text_file = open("../final_project/poi_names.txt", "r")
# lines = text_file.readlines()
# print lines
# temp = lines[2:]
# print "\n\n\n\n"
# print len(temp)
# text_file.close()

#What is the total value of the stock belonging to James Prentice?
#print(enron_data['PRENTICE JAMES']['total_stock_value'])

#How many email messages do we have from Wesley Colwell to persons of interest?
#print enron_data['COLWELL WESLEY']['from_this_person_to_poi']


#Whats the value of stock options exercised by Jeffrey K Skilling?
#print enron_data['SKILLING JEFFREY K']['exercised_stock_options']

# salaryCount,emailCount = 0,0
# print salaryCount
#How many folks in this dataset have a quantified salary? What about a known email address?
# for i in d.values():
# 	if(i['salary'] != "NaN"):
# 		salaryCount+=1

# 	if(i['email_address'] != "NaN"):
# 		emailCount+=1

# print salaryCount,emailCount

#More More More :

# How many people in the E+F dataset have NaN as their total payments. What percentage of people in the dataset as a whole is this
# haveTP,nothaveTP = 0.0,0.0
# for i in d.values():
# 	if(i['total_payments'] == "NaN"):
# 		haveTP+=1
# 	else:
# 		nothaveTP+=1
# print haveTP,nothaveTP
# percentage = haveTP/(haveTP+nothaveTP)
# print "Percentage of people have NaN are",percentage*100

"""How many POIs in the E+F dataset have NaN for their total payments What percentage of POI as a whole is this"""


# countPoiTP = 0
# for i in d.values():
# 	if(i["poi"] == True and i['total_payments'] == "NaN"):
# 		countPoiTP+=1
# print countPoiTP


"""If you added in, say, 10 more data points which were all POIs, and put NaN for the total payments for those folks, the numbers you just calculated would change.
What is the new number of people of the dataset What is the new number of folks with NaN for total payments """


# haveTP,nothaveTP = 10.0,0.0
# for i in d.values():
# 	if(i['total_payments'] == "NaN"):
# 		haveTP+=1
# 	else:
# 		nothaveTP+=1
# print haveTP,nothaveTP








