miles = input("please input your miliage(number please): ")
kilometers_driven = float(miles)/1.6
galons = input("pleaase input your galon used(number please): ")
liters = float(galons)/3.89
L_per_100km = 100*liters/kilometers_driven
print("kilometers driven = ",kilometers_driven,"liters used = ",liters,"L per 100km = ",L_per_100km)