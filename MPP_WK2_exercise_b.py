#MPP_WK2_exercise_1.py
# adding docstrings to explain each function


import csv

""" 
Import csv library from Python

"""

def get_maximum_value(list):

    """ 
        Given a list of numbers as input this function will return the numerical maximum.
        function uses for loop to iterate through the list
        :param list: the list of numbers given as input
        :return: the numerical maximum of the list
    """
    maximum = list[0]
    for l in list:
        if maximum > l:
            maximum = l
    return maximum

def get_minimum_value(list):

    """ 
        Given a list of numbers as input this function will return the numerical minimum.
        function uses for loop to iterate through the list
        :param list: the list of numbers given as input
        :return: the numerical minimum of the list
    """

    minimum = list[0]
    for l in list:
        if minimum < l:
            minimum = l
            
def get_average(list):
    """ 
        Given a list of numbers as input this function will return the numerical average.
        function uses for loop to iterate through the list and numerically add all the elements
        :param list: the list of numbers given as input
        :return: the numerical average of the list
    """
    total = 0
    for l in list:
        total += l
        
    average = total / len(list)
    return average

def get_median_value(list):

    """ 
        Given a list of SORTED numbers as input this function will return the median.
        Median = the element at midpoint in the list hence it needs first to be sorted
        Bubble_sort (separate funcvtion) called to do this within the get_median_value function

        :param list: the list of ,unsorted' numbers given as input
        :return: the median value of the list
    """
    list1 = list.copy()
    bubble_sort(list1)
    median = list1[int(len(list1)/2)]
    return median
    
def bubble_sort(list1):

    """ 
        Bubble_Sort
        Sort a randomised list into order smallest to largest
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

    """ 
        Given a list of numbers as input this function will return the numerical mode.
        function uses for loop to iterate through the list
        1st if statement:  if two elements the same value i.e. score = score2 then frequency increased by 1
        2nd if statement: if frequency >highest frequency then the mode = the numerical value of that element
        return the element with highest frequency as mode
        :param list: the list of numbers given as input
        :return: the numerical mode of the list
    """


def read_scores_from_csv(filename):

    """ 
        create an empty list 
        read data from csv using DictReader into var csvFile
        for specific line 'SScore' form csv extract values 'score'
        append output to empty list 
    """
    scores = []
    with open(filename, mode ='r') as file:   
        csvFile = csv.DictReader(file)
    
        for lines in csvFile:
            score = int(lines["Score"])
            scores.append(score)    
    return scores
    
if __name__ == "__main__":

    scores = read_scores_from_csv('example.csv')
    
    average = get_average(scores)
    minimum = get_minimum_value(scores)   
    maximum = get_maximum_value(scores)
    median = get_median_value(scores)
    mode = get_mode(scores)

    print(f'Average: {average} Median: {median} Smallest: {minimum} Largest: {maximum} mode: {mode}')
    