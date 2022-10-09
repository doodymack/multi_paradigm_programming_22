# MPP_WK2_exercise_5.py
# bring in data from a separate column in the CSV file

import csv

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
    
def bubble_sort(list1):

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


def get_variance(list):

    numerator = 0

    diff_from_mean = []

    for i in range(0, len(list),1):

        diff_from_mean.append(list[i]-average)
        numerator = numerator + (diff_from_mean[i]**2)

    variance =numerator/len(list)
    return variance



def get_std_dev(array):
    mean = get_average(array)
    for i in array:
        array = (i - mean) ** 2
        return array
    sum_sqr_diff = 0
    for i in array:
        sum_sqr_diff = sum_sqr_diff + i
        return sum_sqr_diff
    variance = 1/len(array)
    mean_sqr_diff = (variance * sum_sqr_diff)
    
    std_dev = math.sqrt(mean_sqr_diff)
    return std_dev


def read_scores_from_csv(filename):

    """ 
        create an empty list 
        read data from csv using DictReader into var csvFile
        for specific line 'SScore' form csv extract values 'score'
        append output to empty list 
    """


    # Write a new function to bring in data from a separate column in the CSV file,
    # can you do this by modifying the existing method to be more generalised?
    # Consider default parameters (this is a language feature of Python).

    # Should me a simple modification of the below code but Need help with this!


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
    variance = get_variance(scores)
    stdev = get_std_dev(scores)

    print(f'Average: {average} Median: {median} Smallest: {minimum} Largest: {maximum} mode: {mode} variance: {variance} standard deviation: {stdev}')
    