def validWord(grayLetters, yellowLetters, greenLetters, word):
	for letter in grayLetters:
		if letter in word:
			return False
	for letterLocation in yellowLetters:
		if word[int(letterLocation[1])] == letterLocation[0] or letterLocation[0] not in word:
			return False
	for letterLocation in greenLetters:
		if word[int(letterLocation[1])] != letterLocation[0]:
			return False
	return True

def getUserInput():
	grayLetters = input("Enter the (new!) letters that appear grayed out. For example, \"fhe\": ")
	yellowLetters = input("Next, enter (new!) yellow letters and their indecies. For exmaple, \"a0 t4\": ")
	greenLetters = input("Lastly, enter (new!) green letters and their locations: ")
	return grayLetters, yellowLetters.split(" ") if yellowLetters != "" else [], greenLetters.split(" ") if greenLetters != "" else []

def checkCorrectGuess():
	yesAnswers = ["y", "Y", "Yes", "YEs", "YES", "yES", "yeS", "yEs"]
	if input("Was your guess correct? y/n") in yesAnswers:
		print("Nice! Exiting now...")
		exit()

if __name__ == "__main__":
	f = open("valid-wordle-words.txt", "r")
	print("Welcome to the wordle solver. To begin, enter your first guess into Wordle. (I reccommend crane)")	
	grayLetters, yellowLetters, greenLetters = getUserInput()  
	myWords = []
	myLine = f.readline()
	while myLine != "":
		if validWord(grayLetters, yellowLetters, greenLetters, myLine):
			myWords.append(myLine[:-1])
		myLine = f.readline()
	
	tries = 1
	while tries < 5:
		print("Here are words that could work:")
		print(myWords)
		print("Please guess one")
		checkCorrectGuess()
		grayLetters, yellowLetters, greenLetters = getUserInput()
		newWords = []
		for word in myWords:
			if validWord(grayLetters, yellowLetters, greenLetters, word):
				newWords.append(word)
		myWords = newWords
		tries += 1 
	print("Here are words that could work:")
	print(myWords)
	checkCorrectGuess()
	print("Unlucky! You'll get the word next time. Remember that Wordle seems to favor more common words. You can also try words that have letters that are all unqiue.")

