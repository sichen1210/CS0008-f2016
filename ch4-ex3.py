RT = 0
BG = input('your budget for please:')
TIME = 1
while TIME > 0:
    EX = float(input('your expense:'))
    TIME = TIME + 1
    RT = RT + EX
    LEFT = BG - RT
    if LEFT >= 0:
        print('you are under your budget by'+ str(LEFT))
    else:
        LEFT = 0 - LEFT
        print('you are over your budget by'+ str(LEFT))