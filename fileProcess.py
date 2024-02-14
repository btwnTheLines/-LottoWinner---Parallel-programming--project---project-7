###
#   FILE NAME PROCESSING AND FORMATTING
###
def processData(entriesFileName):
    #get the name of the entry file
    #place the name into a variable for later use
    extRemName = entriesFileName.replace('.csv','')
    winningNumFile = extRemName + ' result.csv'
    countryFileName = extRemName + '_matchResultsFile.csv'

    nameData = {
        'winningNumFile': winningNumFile,
        'countryFileName': countryFileName
    }

    return nameData