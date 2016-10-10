width1 = input("please input width of rectangular 1: ")
width_1 = float(width1)
width2 = input("please input width of rectangular 2: ")
width_2 = float(width2)
length1 = input("please input length of rectangular 1: ")
length_1 = float(length1)
length2 = input("please input length of rectangular 2: ")
length_2 = float(length2)
area_1 = width_1 * length_1
area_2 = width_2 * length_2
if area_1 > area_2:
    print("rectangular 1 is larger")
elif area_2 > area_1:
    print("rectangular 2 is larger")
else:
    print("rectangular 1 and rectangular 2 have same area")