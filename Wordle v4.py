wordle = open("Wordle.txt", "r")
wordList = []
for line in wordle:
    stripped_line = line.strip()
    wordList.append(stripped_line)
#mutableList = []
#outcomeList = []
listDict = {0: wordList}
guessCount = 0


def blackLetter(letter, list, count):
    for word in list:
        if not letter in word:
            listDict[count + 1].append(word)


def greenLetter(letter, location, greenList, count, dicti):
    mutableList = []
    print(greenList)
    for word in greenList:
        print(word)
        if word[location] == letter:
            mutableList.append(word)
            print(word)
            #dicti.update({count + 1: word})
            continue
        else:
            print(word)
            continue
    dicti.update({count + 1 : mutableList})


# def moreGreenLetter(letter, location, greenList):
#     for word in greenList:
#         if word[location] == letter:
#             #mutableList.append(word)
#             print(word)
#             continue
#         elif word[location] != letter:
#             print(word + "ohoh")
#             print(mutableList)
#             mutableList.remove(word)
#             print(mutableList)
#             #greenList.remove(word)

while guessCount < 30:
    guessColor = input("What color? ")
    guessLetter = input("What letter? ")
    if guessColor.lower() == "g":
        guessSpot = int(input("What position? ")) - 1
        greenLetter(guessLetter, guessSpot, listDict[guessCount], guessCount, listDict)
        print(listDict[guessCount + 1])
    # elif guessColor.lower() == "y":
    #     guessSpot = input("What position?") - 1
    #     yellowLetter(guessLetter, guessSpot, listDict[guessCount])
    elif guessColor.lower() == "b":
        blackLetter(guessLetter, listDict[guessCount], guessCount)
        print(listDict[guessCount + 1])
    elif guessColor != any("gby"):
        break
    guessCount += 1

# greenLetter("y", 4, listDict[0])
# moreGreenLetter("s", 0, listDict[1])
#print(wordList)
#print(mutableList)
