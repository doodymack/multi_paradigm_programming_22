# MPP_WK2_exercise_4.py
# added two new python functions variance and standard deviation

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


#derived from: https://medium.com/geekculture/write-your-own-statistical-functions-using-python-bc2c45a3aa39

# Define the variable, numerator, and initialise it to 0.
# Define a blank list, diff_from_mean, which will hold the values of the difference from the mean of all of the elements in the list, x.
# Create a for loop that will iterate from 0 to the length of x. It will append the difference of the mean for each element into the list.
# The variable, numerator, is composed of the square root of the difference of the mean for each element in the list, x.
# Once the for loop has completed its iterations, the variable, variance_x will be defined that will be composed of the numerator divided by the length of the list, x.
# The function will then return the variable, variance_x.#

def get_variance(list):
   # Define the variable, numerator, and initialise it to 0. 
    numerator = 0
   # Define a blank list, diff_from_mean, which will hold the values of the difference from the mean of all of the elements in the list, x.
    diff_from_mean = []
    # Create a for loop that will iterate from 0 to the length of x. It will append the difference of the mean for each element into the list.
    for i in range(0, len(list),1):
    # The variable, numerator, is composed of the square (error in ref above says 'square root') of the difference of the mean for each element in the list, x.
        diff_from_mean.append(list[i]-average)
        numerator = numerator + (diff_from_mean[i]**2)
    # Once the for loop has completed its iterations, the variable, variance_x will be defined that will be composed of the numerator divided by the length of the list, x.
    # The function will then return the variable, variance_x.

    # should this not be len-1? 
    variance =numerator/len(list)
    return variance



# derived from https://stackoverflow.com/questions/70087607/how-do-i-calculate-standard-deviation-in-python-without-using-numpy
# requires to use the mean(average) so refers out to get_average function
# hence function within a function
# note list here called array - still works
def get_std_dev(array):
    # get mu
    mean = get_average(array)
    # (x[i] - mu)**2
    for i in array:
        array = (i - mean) ** 2
        return array
    sum_sqr_diff = 0
    # get sigma
    for i in array:
        sum_sqr_diff = sum_sqr_diff + i
        return sum_sqr_diff
    # get mean of squared differences
    variance = 1/len(array)
    mean_sqr_diff = (variance * sum_sqr_diff)
    
    std_dev = math.sqrt(mean_sqr_diff)
    return std_dev


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
    