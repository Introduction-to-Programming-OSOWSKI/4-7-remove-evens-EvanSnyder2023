def removeEvens(k):
    myList = k
    word = 0
    for i in range(0, len(k)):
        if myList[i - word] % 2 == 0 and myList[i - word] != 0:
            myList.pop(i - word)
            word = word + 1

    return myList

print (removeEvens([1,2,3,4]))