#a1_t7.py
#This program is to check the Air Quality
carbondioxide_data = 750 #The Carbon dioxide is assigned a data in ppm
if carbondioxide_data >=400 and carbondioxide_data < 700: #Conditions for checking air Quality
    print("The Air Quality is EXCELLENT")
elif carbondioxide_data >= 700 and carbondioxide_data < 900:
    print("The Air Quality is GOOD")
elif carbondioxide_data >= 900 and carbondioxide_data < 1100:
    print("The Air Quality is FAIR")
elif carbondioxide_data >= 1100 and carbondioxide_data < 1600:
    print("The Air Quality is MEDIOCRE- Contaminated indoor air, Ventillation recommended")
elif carbondioxide_data >= 1600 and carbondioxide_data <=2100:
    print("The Air Quality is BAD- Heavily contaminated indoor air, Ventillation required")
