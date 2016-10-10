number = input("please in put how many cookies you want to make(numbers please): ")
Number = int(number)
sugar_per_cookie = 300/48
buttes_per_cookie = 240/48
flour_per_cookie = 330/48
sugar_needed = Number * sugar_per_cookie
buttes_needed = Number * buttes_per_cookie
flour_needed = Number * flour_per_cookie
print("you need sugar:"+str(sugar_needed)+"g  ""buttes:"+str(buttes_needed)+"g  ""flour:"+str(flour_needed)+"g.")
