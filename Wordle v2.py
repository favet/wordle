wordle = open("Wordle.txt", "r")
wordList = []
for line in wordle:
    stripped_line = line.strip()
    wordList.append(stripped_line)
blackSet = set("yim")
yellowSet = set("ae")
yellowDict = {"e": 0, "a": 1}
yellowKeys = yellowDict.keys()
greenDict = {"s": 0, "t": 1}
greenKeys = greenDict.keys()

afterYellow = []
testList = []
dictlength = len(yellowKeys)
print(dictlength)
print(yellowSet)


def checkforyellow(yellowIn, yellowOut, wordCheck=0):
    for word in yellowIn:
        if blackSet.isdisjoint(word):
            for key in yellowKeys:
                if wordCheck == len(yellowKeys):
                    print(word)
                    yellowOut.append(word)
                    break
                elif word[yellowDict[key]] == key:
                    break
                elif key not in word:
                    break
                elif key in word:
                    print(word)
                    wordCheck += 1
                else: break


def checkforgreen(greenIn, greenOut, wordCheck=0):
    for word in greenIn:
        for key in greenKeys:
            if word[greenDict[key]] != key:
                break
            elif wordCheck < len(greenKeys):
                wordCheck += 1
                continue
            else:
                greenOut.append(word)
                break


checkforyellow(wordList, afterYellow)
checkforgreen(afterYellow, testList)
finalList = list(dict.fromkeys(testList))
print(wordList)
print(afterYellow)
print(finalList)
print(testList)
