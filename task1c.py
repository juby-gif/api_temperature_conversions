def f_to_k(f):
    k = (f-32) * 5/9 + 273.15 #Formula to convert Fareheit to Kelvin
    return k #Return the value of k to where it stopped(line 5)
f = 100.0
k = f_to_k(f)
print("Fareheit of " + str(f) + "  is " + str(k) + " in Kelvin")
