speed = int(input('your speed:'))
Time = int(input('how long have you travelled: '))
time = 1
if Time < 1:
    print("error, your travel time is less than one hour!")
while time < Time:
    D = speed * time
    time = time + 1
for time in range[1,Time,1]:
    print("Hour"       "distance")
    print( time,          D)
    