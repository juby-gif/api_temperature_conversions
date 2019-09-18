#a1_t6.py
#This program is to find the Range,Single mode Value,Double mode value,Standard deviation and Variance
#taking advantage of python statistics library
import statistics #import statistics library
data_arr = [3,5,11,2,1,4,6,2,4,3,1,10,3] #data_arr is assigned a list of elements

print("the Range of the array is", statistics.range(data_arr))
#print the range using statistics.range()

print("The Single Mode Value of the array is ", statistics.mode(data_arr))
#Print the single mode value using mode() function

print("The Standard Deviation of the array is ", statistics.stdev(data_arr))
#print standard deviation using stdev() function

print("The Variance of the array is ", statistics.variance(data_arr))
#Print the variance using pvariance() function
