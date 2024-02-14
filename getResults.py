def getResults(perf_counter, fileProcess, entriesFile, WinningEntry, UserEntries, threading):

    start_time = perf_counter()

    nameData = fileProcess.processData(entriesFile)

    ###
    #   WINNING ENTRY DATA EXTRACTION SECTION
    ###

    #Create objects
    winningObj = WinningEntry.WinningEntry()
    userObj = UserEntries.UserEntries()

    #Create threads and process data using methods
    threadInner1 = threading.Thread(winningObj.openWinningFile(nameData))
    threadOuter2 = threading.Thread(userObj.processUserEntries(nameData, entriesFile, winningObj))

    #Start threads
    threadInner1.start()
    threadOuter2.start()

    #Join threads so they terminate together
    threadInner1.join()
    threadOuter2.join()

    end_time = perf_counter()

    #Print speed of function
    print(f"\n------ Time of multithreaded functions - {end_time- start_time: 0.2f}")