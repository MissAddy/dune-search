def getWord():
    word = input("Enter the word you want defined here: ")
    return word

def saveWord():
    global desiredWord
    desiredWord = getWord()

