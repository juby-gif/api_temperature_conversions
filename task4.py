pressure_arr = [80, 90, 100, 150, 120, 110, 160, 110, 100]
i = 0
a = 0
sum = 0
mean = 0
count = len(pressure_arr) #To get the length of blood pressure list
print(count) #To print the length
while i < count: #To  find the sum of all elements in the list
    a = pressure_arr[i]
    i = i + 1
    sum = sum + a #Total sum of elements
mean = sum/count #Formula to find the mean
print("The Mean Value of Blood Pressure is", mean, "mm of Hg")
