#a1_t4.py
# This code takes a list of integers and find mean by
#taking advantage of python statistics library
import statistics
pressure_arr = [80, 90, 100, 150, 120, 110, 160, 110, 100]
mean = statistics.mean(pressure_arr)
print("The Mean Value of Blood Pressure is", mean, "mm of Hg")
