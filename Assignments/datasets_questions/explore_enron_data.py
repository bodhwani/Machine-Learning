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

# print enron_data
temp = []
for i in enron_data.values():
	#temp = [x for x in i['exercised_stock_options']]
	#temp =[x for x in i['exercised_stock_options']]
	temp.append(i['exercised_stock_options'])

sortTemp = temp.sort()
print "lenght is ",len(temp)
print "temp is ",temp
ans = []
for i in temp:
	if(i != "NaN"):
		ans.append(i)
print "\n\n\n\n"
print sorted(ans)

# print "Sorted temp is ",sortTemp

# temp = []
# for value in enron_data.values():
# 	temp.append(value['salary'])

# print temp
# print "\n\n\n\n"
# sortedTemp = sorted(temp)
# print sortedTemp

#92384903274


