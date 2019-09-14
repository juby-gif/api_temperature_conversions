power_arr = [4, 5, 2, 6, 3, 7, 8, 9, 6, 5, 2] #Power Meter Readings measured in Kw/h
count = len(power_arr) #To count the number of elementsin the array
print(count)
new_power_arr = sorted(power_arr) # Sorting the array in ascending order
print(new_power_arr)
term = ((count + 1) / 2) - 1 #Formula for finding the position of the median for an odd elemented array
median = new_power_arr[int(term)] #Locating the Median with the position
print("The Median Value of the Power Readings is", median,"which is in position",int(term))
