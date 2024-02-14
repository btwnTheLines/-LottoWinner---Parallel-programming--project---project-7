import csv, DataProcessing, MatchList

class UserEntries:
    def __init__(self):
        pass
        self.matchList = MatchList.MatchList()

    dataDict = {
    #user entry data
    'userID':'',
    'userMainBall':'',
    'userSubBall1':'',
    'userSubBall2':'',
    }

    processor = DataProcessing.DataProcessing()

    ###
    #       USER ENTRIES DATA EXTRACTION SECTION
    ###
    def processUserEntries(self, nameData, entriesFile, winningObj, processor=processor):

        #create results folder based on country using write mode
        with open(nameData['countryFileName'],'w') as results:

            #create writer object
            resultsFileWriter= csv.writer(results)

            #write the headings for the columns
            resultsFileWriter.writerow(['ticket_id','main matches','sub1 matches', 'sub2 matches'])

            #open the user entries file
            with open(entriesFile) as entriesFile:

                #create file reader object
                entriesFileReader = csv.reader(entriesFile, delimiter=';')
                lineCounter = 0

                #print("\n Going into entries for loop")
                #extract data from winning file 
                #going over each row in the entries file
                for row in entriesFileReader:
                    #print("LOOK HERE ", row)
                    #print("\nMatchList = ", self.matchList.matches)
                    #if first line being read
                    if lineCounter == 0:
                        lineCounter += 1;
                    elif len(row):
                        #if the row has no data then len(row) = 0 = false, skip that row
                        #if the row has data in it then len(row) = 1 = true, extract the data
                        self.dataDict['userID'] = row[0]
                        self.dataDict['userMainBall'] = row[1]
                        self.dataDict['userSubBall1'] = row[2]
                        self.dataDict['userSubBall2'] = row[3]

                        #split the main number into individual numbers
                        winningNumbers = winningObj.winningDataDict['winningBallMain'].split(':')
                        userNumbers = self.dataDict['userMainBall'].split(':')

                        #print("winning numbers = ", winningNumbers)
                        #print("user numbers = ", userNumbers,"\n")

                        processor.compareNumbers(self.matchList.matches, winningNumbers, userNumbers)
                        
                        #store sub ball matches
                        if winningObj.winningDataDict['winningSubBall1'] and self.dataDict['userSubBall1'] == winningObj.winningDataDict['winningSubBall1']:
                            self.matchList.matches[6] = 1
                            #print('changed subball 1 match to 1')
                        elif winningObj.winningDataDict['winningSubBall1']:
                            self.matchList.matches[6] = 0
                            #print('changed subball 2 match to 0')

                        if winningObj.winningDataDict['winningSubBall2'] and self.dataDict['userSubBall2'] == winningObj.winningDataDict['winningSubBall2'] :
                            self.matchList.matches[7] = 1
                            #print('changed subball 2 match to 1')
                        elif winningObj.winningDataDict['winningSubBall2']:
                            self.matchList.matches[7] = 0
                            #print('changed subball 2 match to 0')

                        lineCounter+=1

                        #Get the sum of all ball matches
                        matchTotal = sum(self.matchList.matches)

                        #write values to results file based on country 
                        #different counties have different ball sets
                        processor.writeResults(self.matchList.matches, winningObj.winningDataDict, resultsFileWriter, row, matchTotal)

                        #print("\n","END OF DOC",self.dataDict)
                        #print("END OF DOC","LOOK HERE 2 ", row)
                        #print("\n","END OF DOC",self.matchList.matches)

    