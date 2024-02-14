import csv

class WinningEntry: 
    
    winningDataDict = {
        #winning entry data
        'winningBallMain':'',
        'winningSubBall1':'',
        'winningSubBall2':''
    }

    ###
    #   WINNING ENTRY DATA EXTRACTION SECTION
    ###
    
    def openWinningFile(self, nameData):
        #open the winning ticket file
        #print("Inside=",nameData)
        with open(nameData["winningNumFile"]) as winFile:

            #create file reader algorithm
            winFileReader = csv.reader(winFile, delimiter=';')
            lineCounter = 0
            #print("\nGoing into winning for loop\n")

            #extract data from winning file 
            for row in winFileReader:
                #if first line being read
                if lineCounter == 0:
                    #print(row)
                    lineCounter += 1
                #if the row has no data then len(row) = 0 = false, skip that row
                #if the row has data in it then len(row) = 1 = true, extract the data
                elif len(row):
                    self.winningDataDict['winningBallMain'] = row[0]
                    self.winningDataDict['winningSubBall1'] = row[1]
                    self.winningDataDict['winningSubBall2'] = row[2]
                    lineCounter += 1

                    #print("\n",row,"\n")
                

                lineCounter += 1

            #print("\nFinished #printing")
        
