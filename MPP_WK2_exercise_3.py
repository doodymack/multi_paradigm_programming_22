#MPP_WK2_exercise_3.py
# no doc string
# demonstrate move a function (bubble_sort) to a new file and import

import csv

# demonstration of importing a function/def from a separate file
from MPP_WK2_exercise_functions import bubble_sort

def get_maximum_value(list):

    maximum = list[0]
    for l in list:
        if maximum > l:
            maximum = l
    return maximum

def get_minimum_value(list):

    minimum = list[0]
    for l in list:
        if minimum < l:
            minimum = l
            
def get_average(list):

    total = 0
    for l in list:
        total += l

    average = total / len(list)
    return average

def get_median_value(list):

    list1 = list.copy()
    bubble_sort(list1)
    median = list1[int(len(list1)/2)]
    return median
    
#bubble sort function removed
    
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
    