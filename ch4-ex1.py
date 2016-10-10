RT = 0
days = 1
while days <= 5:
    NB = int(input('your number of bugs collected: '))
    while NB < 0:
        print('error')
    RT = RT + NB
    days = days + 1
print(format(RT,'d'))