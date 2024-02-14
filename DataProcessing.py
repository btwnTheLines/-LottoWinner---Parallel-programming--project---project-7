class DataProcessing:
    def __init__(self):
            pass
    
    @staticmethod
    def compareNumbers(storageList, numList1, numList2):
        
        numCounter = 0

        #Count number of matches
        for eachNumber in numList1:
            #if the user entry matches the number
            #print("Testing",eachNumber,"and",numList2[numCounter])
            if eachNumber == numList2[numCounter]:
                #if equal count it as a match
                #print("They are equal")
                #print('number counter =',numCounter)
                #print('\n')
                storageList[numCounter] = 1
                numCounter+=1
                #print(storageList,'\n\n')
            else:
                #if not equal, reset counter to 0
                #print("They are not equal")
                #print('number counter =',numCounter)
                #print('\n')
                storageList[numCounter] = 0
                numCounter+=1
                #print(storageList,'\n\n')

    @staticmethod
    def writeResults(list, dict, fileWriter, row, matchTotal):
        #if sub ball 1 >0 and sub ball 2 > 0 - run
        if dict['winningSubBall1'] and dict['winningSubBall2']:
            #write row into results file, remove sub balls from total to get main balls
            fileWriter.writerow([str(row[0]),str(matchTotal-list[6]-list[7]),str(list[6]), str(list[7])])
            #print('first IF')
            #print('subball1 is',str(list[6]))
            #print('subball2 is',str(list[7]))
        #if sub ball 1 > 0 - run
        elif dict['winningSubBall1']:
            fileWriter.writerow([str(row[0]),str(matchTotal-list[6]-list[7]),str(list[6])])
            #print('second IF')
            #print('subball1 is',str(list[6]))
            #print('subball2 is',str(list[7]))
        #if no sub balls - run
        else:
            fileWriter.writerow([str(row[0]),str(matchTotal)])
            #print('third IF')
            #print('subball is',str(list[6]))
            #print('subball2 is',str(list[7]))