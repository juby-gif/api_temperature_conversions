#a1_t1c.py
#This program is to convert Fareheit to Kelvin
def f_to_k(f):
    k = (f-32) * 5/9 + 273.15 #Formula to convert Fareheit to Kelvin
    return k 
f = 100.0
k = f_to_k(f)
print("Fareheit of " + str(f) + "  is " + str(k) + " in Kelvin")
