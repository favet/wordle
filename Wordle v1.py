blackSet = set("yim")
yellowSet = set("cb")
yellowDict = {"c": 1, "b": 0}
yellowKeys = yellowDict.keys()
greenDict = {"t": 1, "p": 0}
greenKeys = greenDict.keys()
wordList = ["rclll", "cmmbllc", "ptrllbc", "prtll", "srtllbc", "sorll", "ptwerllcb"]
afterYellow = []
testList = []
dictlength = len(yellowKeys)
print(dictlength)
print(yellowSet)


def checkforyellow(yellowIn, yellowOut):
    for word in yellowIn:
        if blackSet.isdisjoint(word):
            print("y")
            for key in yellowKeys:
                print("e")
                if key in word:
                    print("3")
                    if word[yellowDict[key]] != key:
                        print("s")
                        print(word)
                        yellowOut.append(word)
def checkforgreen(greenIn, greenOut):
    for word in greenIn:
        for key in greenKeys:
            print("1")
            if key in word:
                print("2")
                if word[greenDict[key]] == key:
                    print("4")
                    print(word)
                    greenOut.append(word)


checkforyellow(wordList, afterYellow)
checkforgreen(afterYellow,testList)
finalList = list(dict.fromkeys(testList))
print(wordList)
print(afterYellow)
print(finalList)
print(testList)