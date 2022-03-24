word = "salt"
lives = 6
listword = []
listword = ("_ " * len(word)).split()
pword = ""
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

while lives > 0:
	guess = input("Guess a letter: ")
	n = 0
	found = False
	
	for i in word:
		sample = word[n]
		if sample == guess:
			listword[n] = guess
			found = True
		n += 1

	if found == False:
		lives -=1

	if "_" not in listword:
		print("You win.")
		lives = 0
	else:
		print(stages[lives])
	
	for i in listword:
		pword += i
		
	print(listword)



