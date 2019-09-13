def c_to_k(c):
    k = c + 273.15 #Formula to convert Celsius to Kelvin
    return k #Return the value of k to where it stopped(line 10)
def f_to_c(f):
    fa = (f-32) * 5/9 #Formula to convert Fareheit to Celsius
    return fa #Return the value of fa to where it stopped(line 11)
c = 25.0
f = 100.0

k = c_to_k(c)
fa = f_to_c(f)

print("Celsius of " + str(c) + "  is " + str(k) + " in Kelvin")
print("Farenheit of " + str(f) + "  is " + str(fa) + " in Celsius")
