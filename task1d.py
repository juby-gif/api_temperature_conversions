def k_to_c(k):
    c = k - 273.15 #Formula to convert Kelvin to Celcius
    return c #Return the value of c to where it stopped(line 5)
k = 360.0
c = k_to_c(k)
print("Kelvin of " + str(k) + "  is " + str(c) + " in Celcius")
