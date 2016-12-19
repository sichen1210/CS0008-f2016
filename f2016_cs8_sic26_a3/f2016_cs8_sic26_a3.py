#This program is done by Nov. 18 2016
#done by      Si Chen
#emial: sic26@pitt.edu
#assignment relates to function, dictionary, loop, list, files.


#We are asked to write a program that read the master input list file, retrieves the names of the data files and from
#each one of them reads every line, extract name and distance. Once the program has all the data in memory, it has to
#compute the following quantities and informations:
##    • number of files read in input
##    • total number of lines read
##    • total distance run
##    •total distance run for each participants
##    • individual maximum distance run and by which participant
##    • individual minimum distance run and by which participant
#    • report if there are any participants that appears more than once, how many times and their names
##    • total number of participants

#The program should provide an terminal output similar to the following:
#    Number of Input files read      : xx
#    Total number of lines read      : xx
#    total distance run              : xxxx.xxxxx
#    by participant                  : participant name
#    max distance run by participan  : xxxx.xxxxx
#    min distance run                : xxxx.xxxxx
#    by participant                  : participant name
#    Total number of participants    : xx
#    Number of participants with multiple records : xx

#The program should also create an output file reporting name of the participant, how many times their name appears in
#the input files and the total distance run. Each row should be as follows:
#    Max,3,124.23
#    Barbara,2,65.00
#    Luka,1,12.87
#    ...


#initialize an empty list L

L = []

#Firstly, open master file and get three file names
#get rid of the "\n"
#open files and get all information in side and put them inside the list L
# MN: why not asking the user for the master list file name
fn = open('f2016_cs8_a3.data.txt','r').readlines()
for item in fn:
    L = L + open(item.strip('\n')).readlines()
#loop end file closed



#get rid of the "\n"
# write in comprehensive way and create a long list C
C = [item.strip('\n').split(',') for item in L]

# get rid of the header
for item in C:
    if "distance" in item:
        C.remove(item)
#loop end

#number of files read in input
NF_in_input = len(fn)

#total number of lines read
TTN_of_lines = len(L)


#Use dictionary to solve the rest of problems
#define dictionary
name = {item[0] for item in C}
distance = {item[1] for item in C}

#find the total distance TTD
TTD = sum(float(item) for item in distance)

#distance for same person will be added automatically when convert list to dictionary
record = dict(zip(name,distance))

#total number of participant is
TTN_of_runner = len(record)


# find same names and their counts in the list
# MN: I would like to see more comments. it took me a while to figure out what you were doing
# MN: here you create a list of the names
list = [item[0] for item in C]
# MN: here you create a list where each element is a list of 2 items: name and how many times is found in the list
account1 = [[item, list.count(item)] for item in list]
# MN: here you do the same as before but only for names that show up more than once
account2 = [[item, list.count(item)] for item in list if list.count(item) != 1]
No = len(account2)
for item in account2:
    if item[0] in record.keys():
        account3 = [item.append(record.values())]

#find the maximum and minimum of distance
# MN: are you sure that you are computing the maximum and minumim total distance run by each participant?
#     it seems to me that you are working on each single record 
IMax = max(zip(record.values() ,record.keys()))
IMin = min(zip(record.values(),record.keys()))

#output values to a file
file = open("f2016_cs8_sic26_a3.data.output.csv",'w')

#find the content we need to write inside the file
# MN: I'm not entirely sure that is the best method and that it achieves the functionality
content = [[item,list.count(item),record[item],"\n"] for item in list]
for elem in content:
    file.write(str(content))
file.close()


#provide a out put
print("Number of Input files read        :  ",NF_in_input)
print("total number of lines read        :  ",TTN_of_lines)
print(' ')
print('total distance run                :  ',TTD)
print(' ')
print('max distance run                  :  ',IMax[0])
print('   by participnt                  :  ',IMax[1])
print(' ')
print('min distance run                  :  ',IMin[0])
print('   by participnt                  :  ',IMin[1])
print(' ')
print('total number of participant       :  ',TTN_of_runner)
print('number of participants')
print(' with multiple records            :  ',No)

