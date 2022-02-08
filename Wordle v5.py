wordle = open("Wordle.txt", "r")
wordList = []
for line in wordle:
    stripped_line = line.strip()
    wordList.append(stripped_line)
listDict = {0: wordList}
guessCount = 0

def greenLetter(letter, location, list, count, dicti):
    mutableList = []
    for word in list:
        if word[location] == letter:
            mutableList.append(word)
    dicti.update({count + 1: mutableList})

def yellowLetter(letter, location, list, count, dicti):
    mutableList = []
    for word in list:
        if word[location] != letter and letter in word:
            mutableList.append(word)
    dicti.update({count + 1: mutableList})

def blackLetter(letter, list, count, dicti):
    mutableList = []
    for word in list:
        if not letter in word:
            mutableList.append(word)
    dicti.update({count + 1: mutableList})

while guessCount < 300:
    print("There are " + str(len(listDict[guessCount])) + " words remaining in the game.")
    print("These are your top recommended guesses: " + str(listDict[guessCount][0:5]) + ". ")
    guessColor = input("What color? ")
    guessLetter = input("What letter? ")
    if guessColor.lower() == "g":
        guessSpot = int(input("What position? ")) - 1
        greenLetter(guessLetter, guessSpot, listDict[guessCount], guessCount, listDict)
    elif guessColor.lower() == "y":
        guessSpot = int(input("What position?")) - 1
        yellowLetter(guessLetter, guessSpot, listDict[guessCount], guessCount, listDict)
    elif guessColor.lower() == "b":
        blackLetter(guessLetter, listDict[guessCount], guessCount, listDict)
    elif guessColor != any("gby"):
        continue
    guessCount += 1
