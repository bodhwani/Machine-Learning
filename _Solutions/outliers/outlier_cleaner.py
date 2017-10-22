#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here

    temp = zip(predictions, net_worths)
    
    error = [x-y for x,y in temp]

    
    temp2 = zip(ages,net_worths,error)
    temp2sorted = sorted(temp2, key=lambda x:x[2])
    
    
        
    cleaned_data = temp2sorted[:81]
    

        

    
    return cleaned_data

