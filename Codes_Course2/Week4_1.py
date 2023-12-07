fname = input("Enter file name: ")
finalList = list()
with open(fname) as fh:
    for line in fh:
        words = line.split()
        for i in range(len(words)):
            if words[i] not in finalList:
                finalList.append(words[i])

    finalList.sort()
    print(finalList)
    print(len(finalList))

finalList = list()
with open(fname) as fh:
    for line in fh:
        words = line.split()
        for i in range(len(words)):
            finalList.append(words[i])

    finalList = set(finalList)
    listCheck = list(finalList)
    print(type(listCheck))
    listCheck.sort()

    print(listCheck)
    print(len(listCheck))

