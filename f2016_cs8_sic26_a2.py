#This program is done by OCT. 29 2016
#done by      Si Chen
#emial: sic26@pitt.edu

#assignment related to file object and loop
#chapter4 - chapter6

#two fuctions needed to be defined

#define input function function:

def processFile():
    PTN = int(line)



#define the output function:'

def printkv(key, value, klen=0):
    kl = max(len(key),klen)

#there are three cases that the data in file object may appear:
#string
    if isinstance(value,str):
        FS = '20s'
#integer
    elif isinstance(value,int):
        FS = '10d'
#float
    elif isinstance(value,float):
        FS = '10.3f'
#validation: exclude other posibilities
    else:
        print("error! cannot ecxute.")
    print(format(key, str(kl) + 's'), format(value, FS))

#main body of the program

#first part: collect and excute data
#set initail value as 0

PTN = 0
PD = 0

#open the 1stfile we choose
FO = open("f2016_cs8_a2.data.1.csv","r")
#use loop to excute every value in file object
for line in FO:
#get rid of the "new line" symble
    line = line.rstrip("\n")
#seperate the values
    Temp = line.split(",")
#choose the second value and add it to distance as float
    Dist = float(Temp[1])
    PD += Dist
#change the PD and PTN after excuting every value
    PTN += 1

#print the outcome with certain format
print("File to be read: file_1.csv")
printkv('partial total number of lines:',PTN)
printkv('partial distance:',PD)

#close file
FO.close()

PTN = 0
PD = 0

#open the 2nd file we choose
FO = open("f2016_cs8_a2.data.2.csv","r")
#use loop to excute every value in file object
for line in FO:
#get rid of the "new line" symble
    line = line.rstrip("\n")
#seperate the values
    Temp = line.split(",")
#choose the second value and add it to distance as float
    Dist = float(Temp[1])
    PD += Dist
#change the PD and PTN after excuting every value
    PTN += 1

#print the outcome with certain format
print("File to be read: file_2.csv")
printkv('partial total number of lines:',PTN)
printkv('partial distance:',PD)

#close file
FO.close()




#second part: chhgompute the total value
#set initail total valus as 0:

TTD = 0
TTN = 0

#select the file we want to use:

File = input("f2016_cs8_a2.data.1.csv")

#use while loop to test the condition

while File != " " and File != "quit" and File != "q":
    fh = open(File,"r")
    PD,PTN = processFile(fh)
    fh.close()
    TTD += PD
    TTN += PTN
    Flie = input("f2016_cs8_a2.data.2.csv" )
printkv('total number of lines:',TTN)
printkv('total distance:',TTD)