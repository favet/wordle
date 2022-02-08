wordle = open("Wordle.txt", "r")
wordList = []
for line in wordle:
    stripped_line = line.strip()
    wordList.append(stripped_line)
listDict = {0: wordList}
guessCount = 0

def letterCheck(letter, location, list, count, dicti, color):
    mutableList = []
    if color.lower() == "g":
        for word in list:
            if word[location] == letter:
                mutableList.append(word)
        dicti.update({count + 1: mutableList})
    elif color.lower() == "y":
        for word in list:
            if word[location] != letter and letter in word:
                mutableList.append(word)
        dicti.update({count + 1: mutableList})
    elif color.lower() == "b":
        for word in list:
            if not letter in word:
                mutableList.append(word)
        dicti.update({count + 1: mutableList})
    print(mutableList)

def wordCheck(word, result, list):
    letterCount = 0
    mutableDict = {letterCount : list}
    while letterCount < len(word):
        newList = mutableDict.get(letterCount)
        letterCheck(word[letterCount], letterCount, newList, letterCount + 1, mutableDict, result[letterCount])
        print(mutableDict.get(letterCount))
        letterCount += 1

        #print(mutableDict[letterCount])


input_word = input("what word? ")
input_result = input("what result? ")
test_list = []
wordCheck(input_word, input_result,wordList)

# while guessCount < 26:
#     print("There are " + str(len(listDict[guessCount])) + " words remaining in the game.")
#     print("These are your top recommended guesses: " + str(listDict[guessCount][0:5]) + ". ")
#     guessColor = input("What color? ")
#     guessLetter = input("What letter? ")
#     guessSpot = int(input("What position? ")) - 1
#     letterCheck(guessLetter,guessSpot,listDict[guessCount],guessCount, listDict, guessColor)
#     guessCount += 1
#     print("guessCount = " + str(guessCount))
