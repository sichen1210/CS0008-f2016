# data collection: ask users for information
print("")
system=(input("select the system you want to use, type '1' for USC, '2' for Metric: "))
D = float(input("input distance you have travelled: "))
G = float(input("input how much gas you have used: "))
# get data and convert the units and compute the fuel consumption(MPG)
# DM(distance in mile) GG(gas in gallon) DK(distance in kilometers) GL(gas in liters)
if system == 1:
    DM = D
    GG = G
    DK = 1.60934 * DM
    GL = 3.78541 * GG
    MPG = DM / GG
    cm = 100 * GL / DK
elif system == 2:
    DK = D
    GL = G
    DM = DK * 0.621371
    GG = GL * 0.264172
    MPG = DM / GG
    cm = 100 * GL / DK
else:
    print("error! you need to choose a system! ")
if cm < 0:
    print("error! check your distance and gas value.")
elif cm <= 8:
# GCR is Gas consumption rating
    GCR = "Excellent"
elif cm <= 10:
    GCR = "Good"
elif cm <= 15:
    GCR = "Average"
elif cm <= 20:
    GCR = "Poor"
else:
    GCR = "Extremely Poor"
# output: show the result
print("")
print("                             USC""                  Metric")
print("Distance          :    "+format(DM,'10.3f')+" miles    "+format(DK,'10.3f')+" Km")
print("GAS               :    "+format(GG,'10.3f')+" gallons  "+format(GL,'10.3f')+" Liters")
print("Consumption       :    "+format(MPG,'10.3f')+" mpg      "+format(cm,'10.3f')+" 1/100Km")
print(" ")
print("Consumption rating:    " +GCR)