#MPP_WK2_exercise_1b.py
# adding docstrings to explain each function (I did this twice in error but different approach)

import csv

def get_maximum_value(list):
    """ 
        Given a list of numbers as input this function will return the numerical maximum.
        :param list: the list of numbers given as input
        :return: the numerical maximum of the list
    """    
    # simple search for l with maximum number in list by iterating through the list
    # if l is grreater than l in memory
    # new l replaces old l until end of list
    # l is numerical maximum in list
    # note list doesn't have to be sorted like for median
    maximum = list[0]
    for l in list:
        if maximum > l:
            maximum = l
    return maximum

def get_minimum_value(list):
    """ 
        Given a list of numbers as input this function will return the numerical average.
        :param list: the list of numbers given as input
        :return: the numerical minimum of the list
    """
    # simple search for l with minimum value in list by iterating through the list
    # if l is less than l in memory
    # new l replaces old l until end of list
    # l is numerical minimum in list
    # note list doesn't have to be sorted like for median
    minimum = list[0]
    for l in list:
        if minimum < l:
            minimum = l
            
def get_average(list):
    """ 
        Given a list of numbers as input this function will return the numerical average.
        :param list: the list of numbers given as input
        :return: the numerical average of the list
    """
    total = 0
    for l in list:
        total += l
     # simple average by summing the values in the list iteratively using +=1
     # then dividing by the number of elelemts i.e (len) of list
     # l is numerical average/mean in list
    # note list doesn't have to be sorted like for median  
    average = total / len(list)
    return average

def get_median_value(list):
    """ 
        Given a list of numbers as input this function will return the numerical average.
        :param list: the list of numbers given as input
        :return: the numerical average of the list
    """
    # make a copy of list as 'list 1' that will become the sorted version of 'list'
    list1 = list.copy()
    #use bubble-sort function below to sort the lsit smallest to largest
    bubble_sort(list1)
    # median is the middle value
    # inside brackets is the index number
    # to get the median index divide the length of list1 by 2. convert to integer
    # extract the list1 value at this point as vsriable 'median'
    median = list1[int(len(list1)/2)]
    return median
    
def bubble_sort(list1):

    """ 
        Given an unsorted list list input this function will return the sorted list 
        using recursive bubble-sort algorithm.

        :param list: the list of numbers given as input
        :return: the sorthed list smallest to largets numerically
    """

    for i in range(0,len(list1)-1):  
        for j in range(len(list1)-1):  
            if(list1[j]>list1[j+1]):  
                temp = list1[j]  
                list1[j] = list1[j+1]  
                list1[j+1] = temp  
    
def get_mode(list):
    highest_freq = 0
    mode = scores[0]
    for score in scores:
        frequency = 0
        for score2 in scores:
            if score == score2:
                frequency += 1
        if frequency > highest_freq:
            mode = score
            highest_freq = frequency
    return mode

def read_scores_from_csv(filename):

    """ 
        Given an csv file (filename) the function extracts the values of 'score'
        extract them to a newly created list 'scores'

        :param list: the list of elements in the csv undser 'scores'
        :return: the new 'scores' list
    """ 
    scores = []
    with open(filename, mode ='r') as file:   
        csvFile = csv.DictReader(file)
    
        for lines in csvFile:
            score = int(lines["Score"])
            scores.append(score)    
    return scores
    
    # main program which incorporates the above functions below
    # as they are separate functions they can be in any order or 
    # called from a separate program (see MPP_WK2_exercise_d.py)
    
if __name__ == "__main__":

    scores = read_scores_from_csv('example.csv')
    
    average = get_average(scores)
    minimum = get_minimum_value(scores)   
    maximum = get_maximum_value(scores)
    median = get_median_value(scores)
    mode = get_mode(scores)

    print(f'Average: {average} Median: {median} Smallest: {minimum} Largest: {maximum} mode: {mode}')
    