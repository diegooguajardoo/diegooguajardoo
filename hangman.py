
wordlist = []
initialword = "p e p p e r "
for i in initialword:
	i = i +" "
	wordlist[i] = initialword.split()
disword = ""
hangmanscore = len(initialword)


while hangmanscore > 0:
	print("_" * hangmanscore)
	key = input("Type any letter: ")

	i = 0
	for char in initialword:
		if key == str(initialword[i]):
			initialword[i] = key
			print("reveal")
		
		else:
			print("lost a limb")
			print(hangmanscore)
			hangmanscore -= 1
			i += 1


	for char in initialword:
		disword += char