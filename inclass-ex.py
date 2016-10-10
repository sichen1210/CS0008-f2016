number = input("give me the number: ")
number = int(number)
#I test the range
if number < 0 or number > 36:
    print("give me a number!")
if number == 0:
    color = "green"
elif (number >= 1 and number <= 10) \
     or \
    (number >= 19 and number <= 28):
    if number % 2 == 0:
        color = "black"
    else:
        color = "red"
elif (number >= 11 and number <= 18) \
    or \
    (number >= 29 and number <= 36):
    if number % 2 == 0:
        colore = "red"
    else:
        colore = "black"
print("your color is " + color)
