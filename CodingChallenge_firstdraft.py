# def plaintext(encoded_string):
# 	#this function takes an encoded string, decodes it, and prints it
# 	character_list = list(encoded_string)
# 	#turns the string into a list, sets a variable that stores the list
# 	for i in character_list:
# 	# iterates through list

# 	 	if i.isdigit() == True:
# 	 		# checks if index is a digit
# 	 		true_character = character_list[character_list.index(i) + int(i) + 1]
# 	 			# adds index of digit and 1 to digit to find first true character
# 	 		DECODED_WORD.append(true_character)

# 	 		if i in range(len(character_list)):

# 	 			i = character_list[character_list.index(true_character) + 1]
	 			
# 	 		print ''.join(DECODED_WORD)