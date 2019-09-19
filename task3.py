#a1_t3.py
#This program is to Find minimum and maximum value
temperatures_arr = [21, 23, 26, 22, 25, 20, 19, 23]
max_value = 0
min_value = 0
i = 0
j = 0
count = len(temperatures_arr)
print(count)
while i < count: #To find the maximum temperature value
        temp = temperatures_arr[i]
        i = i + 1
        if temp > max_value:
            max_value = temp
min_value = max_value
while j < count: #To find the minimum temperature value
    new = temperatures_arr[j]
    j = j + 1
    if new < min_value:
        min_value = new
print("The Maximum Temperature value is", max_value, "degrees")
print("The Minimum Temperature value is", min_value, "degrees")
