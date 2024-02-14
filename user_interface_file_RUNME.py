#
# --- NB ---- Files must be in same directory to process them
#

#
#NOTES
#
#Speed vs Readability|Reusability|Modifiability
#
#The latter was chosen, tuples are much faster than lists
#   the data set where lists are used is, however small
#
#The use of dictionaries helps give context, lookup is also faster
# 
#Extensive comments and print statements were used for ease of debugging + modification + the above
#
#
#

import fileProcess, getResults, WinningEntry, UserEntries, threading
from time import perf_counter

###
#   CREATE VARIABLES + DATA STRUCTURES SECTION
###

enteredFile = ''
entriesListFile = []
threadList = []
fileCount = 0

###
#   FILE NAME COLLECTION SECTION
###

while not enteredFile == 'done':
    enteredFile = input("\nPlease enter file name of the entries file:\nEnter 'done' when all file names given\nFile Name:")
    print('fileCOunt internal ', fileCount)
    if not enteredFile == 'done':
        entriesListFile.append(enteredFile)

###
#   THREAD MAKER AND PROCESSING OF FILE/S SECTION
###

for file in entriesListFile:
    threadNameHolder = 'threadInner'+str(fileCount)
    threadNameHolder = threading.Thread(getResults.getResults(perf_counter, fileProcess, entriesListFile[fileCount], WinningEntry, UserEntries, threading))
    threadNameHolder.start()
    threadList.append(threadNameHolder)
    fileCount+=1

fileCount = 0

for file in entriesListFile:
    threadList[fileCount].join()
    fileCount+=1