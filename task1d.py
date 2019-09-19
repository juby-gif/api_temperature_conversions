#a1_t1d.py
#This program is to convert Kelvin to Celsius
def k_to_c(k):
    c = k - 273.15 #Formula to convert Kelvin to Celsius
    return c 
k = 360.0
c = k_to_c(k)
print("Kelvin of " + str(k) + "  is " + str(c) + " in Celsius")
