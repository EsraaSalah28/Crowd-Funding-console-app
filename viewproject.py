def list_project(email):
    listopen = open(email + ".txt", "r")
    for line in listopen:
        Dict = eval(line)
        print("Projects ")
        print(" Title:", Dict['title'], "\n", "Details:", Dict['details'], "\n", "Total:", Dict['total'], "\n",
              "StartDate:", Dict['satartDate'], "\n", "EndDate:", Dict['endDate'])
