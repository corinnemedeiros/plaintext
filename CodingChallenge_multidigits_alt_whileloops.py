
encoded_string = "1uF6YHggr3A4jk09L18L0 5OKerJI0S1h 2kkH3nm3E2BBR7koHYTgRE1d!ppp"

# multi-digit test string: "12oocvz09jqquiH11yywxsanmvbpI13yer6twweop14s 21gebwvsrxeqdwygrtuhijwT11hhllknbvxzdH00E01iR10kkjsagetrdE"
# single-digit test string: "2nsb0u3iohg"

# an empty list to store found characters
DECODED_WORD = []
DECODED_WORD_ALT = []

# plaintext - method to decode an encoded string 
# input - encoded string (Read encoding rules above)
# output - decoded string 
def plaintext(encoded_string):
	
	# converts the encoded string into a list of individual characters
	character_list = list(encoded_string)
	
	length = len(encoded_string)
	i = 0

	# loops through length of list while i is less than list length
	while i < length:
		
		# checks if character at index i is a digit
	 	if character_list[i].isdigit() == True:
	 		
	 		number_of_skips = character_list[i]

	 		while i < length and character_list[i + 1].isdigit() == True:

	 			number_of_skips = int(''.join(character_list[i] + character_list[i + 1]))
	 			
	 			i = i + int(number_of_skips) + 2

	 			if i > length:
	 				print "i is greater than length"
	 				break
	 				
	 			else:
	 				# appends the character to the running decoded alt string
	 				DECODED_WORD_ALT.append(character_list[i])
	 				i += 1
	 			
	 		# total number of characters to skip
	 		i = i + int(number_of_skips) + 1

	 		if i > length:
	 			print "The string is not properly encoded"
	 			break

	 		# appends the character to the running decoded string
	 		DECODED_WORD.append(character_list[i])

	 	i += 1

	print "The decoded string is: " + "\"" + ''.join(DECODED_WORD) + "\""
	print "The decoded string taking multidigits into account is: " + "\"" + ''.join(DECODED_WORD_ALT) + "\""

plaintext(encoded_string)

