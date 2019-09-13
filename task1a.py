def c_to_f(c):
    f = (c * 9/5) + 32 #Formula to convert Celsius to Fareheit
    return f #Return the value of f to where it stopped(line 5)
c = 100.0
f = c_to_f(c)
print("Celsius of " + str(c) + "  is " + str(f) + " in Fareheit")
