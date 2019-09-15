data_arr = [3,5,11,2,1,4,6,2,4,3,1,10,3] #data_arr is assigned a list of elements
import statistics #import statistics library
c = statistics.mode(data_arr) #mode function to find single mode value
l = len(data_arr) #Number of elements in the array
print("the Range of the array is",range(l))
#print the range using range()

print("The Single Mode Value of the array is ", c)
#Print the single mode value using mode()

print("The Standard Deviation of the array is ", statistics.stdev(data_arr))
#print standard deviation using stdev()

print("The Variance of the array is ", statistics.pvariance(data_arr))
#Print the variance using pvariance()
