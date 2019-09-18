#a1_t5.py
#This program is to find the Median of the Smart power meter Readings
#taking advantage of python statistics library
import statistics
power_arr = [4, 5, 2, 6, 3, 7, 8, 9, 6, 5, 2] #Power Meter Readings measured in Kw/h
Median = statistics.median(power_arr)
print("The Median Value of the Power Readings is", Median)
