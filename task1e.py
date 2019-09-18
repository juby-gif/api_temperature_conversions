#a1_t1e.py
#This program is to convert Kelvin to Fareheit.
def k_to_f(k):
    f = (k - 273.15) * 9/5 + 32 #Formula to convert Kelvin to Fareheit
    return f #Return the value of f to where it stopped(line 5)
k = 360.0
f = k_to_f(k)
print("Kelvin of " + str(k) + "  is " + str(f) + " in Farenheit")
