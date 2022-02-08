wordle = open("Wordle.txt", "r")
wordList = []
for line in wordle:
    stripped_line = line.strip()
    wordList.append(stripped_line)
mutableList = []
outcomeList = []

def blackLetter(letter, list):
    for word in list:
        if letter in word:
            list.remove(word)


def greenLetter(letter, location, greenList):
    for word in greenList:
        if word[location] == letter:
            mutableList.append(word)
            continue
        elif word in mutableList:
            mutableList.remove(word)
            #greenList.remove(word)

def moreGreenLetter(letter, location, greenList):
    for word in greenList:
        if word[location] == letter:
            #mutableList.append(word)
            continue
        elif word[location] != letter:
            mutableList.remove(word)
            #greenList.remove(word)

greenLetter("z", 4, wordList)
moreGreenLetter("r", 1, mutableList)
print(wordList)
print(mutableList)

# def checkforyellow(yellowIn, yellowOut, wordCheck=0):
#     for word in yellowIn:
#         if blackSet.isdisjoint(word):
#             for key in yellowKeys:
#                 if wordCheck == len(yellowKeys):
#                     print(word)
#                     yellowOut.append(word)
#                     break
#                 elif word[yellowDict[key]] == key:
#                     break
#                 elif key not in word:
#                     break
#                 elif key in word:
#                     print(word)
#                     wordCheck += 1
#                 else: break
#
#
# def checkforgreen(greenIn, greenOut, wordCheck=0):
#     for word in greenIn:
#         for key in greenKeys:
#             if word[greenDict[key]] != key:
#                 break
#             elif wordCheck < len(greenKeys):
#                 wordCheck += 1
#                 continue
#             else:
#                 greenOut.append(word)
#                 break
