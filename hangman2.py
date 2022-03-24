word = "camel"
score = len(word)
listword = []
listword = ("_ " * len(word)).split()
pword = ""

ltsleft = len(word)

while score > 0:
	guess = input("Guess a letter: ")
	n = 0
	found = False
	
	for i in word:
		sample = word[n]
		if sample == guess:
			listword[n] = guess
			found = True
			ltsleft -= 1
		n += 1

	if found == False:
		score -=1

	if ltsleft == 0:
		print("You win.")
		score = 0
	for i in listword:
		pword += i
		
	print(listword)



