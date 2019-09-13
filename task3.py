temperatures_arr = [21, 23, 26, 22, 25, 20, 19, 23]
max_value = 0
min_value = 0
i = 0
j = 0
k = 0
new = 0
sub_temp = 0
count = len(temperatures_arr) #To find the length of the temperature list
print(count) # To print the length of temperature list
while j < count: #To find the maximum value
    temp = temperatures_arr[j]
    j = j + 1
    if temp > max_value:
        max_value = temp
while i < count: #To find the minimum value
    new = temperatures_arr[i]
    while k < count: #To iterate within the loop for comparing each item in the list
        if temperatures_arr[k] < new:
            sub_temp = temperatures_arr[k]
        k = k + 1
    min_value = sub_temp
    i = i + 1


print("The Maximum Temperature value is", max_value, "degrees")
print("The Minimum Temperature value is", min_value, "degrees")
