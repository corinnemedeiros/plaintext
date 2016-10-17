
encoded_string = "12oocvz09jqquiH11yywxsanmvbpI13yer6twweop14s 21gebwvsrxeqdwygrtuhijwT11hhllknbvxzdH00E01iR10kkjsagetrdE"

# multi-digit test strings: "12oocvz09jqquiH11yywxsanmvbpI13yer6twweop14s 21gebwvsrxeqdwygrtuhijwT11hhllknbvxzdH00E01iR10kkjsagetrdE"
	# "19uhge13btrrdewert9kly00a10nhee!+h89by//pp"

# single-digit test strings: "2nsb0u3iohg" , "3ftgB2mmL0U6ui09vcEopp" , "1uw8hjloiehnh0y" , "3kooB5plie4O0O"
	# caused "ValueError: invalid literal for int() with base 10: '2p'" error: "2poh9nhe62ollte0l13l51urawwo"

# empty lists to store found characters
DECODED_WORD = []
DECODED_WORD_MULTIDIGIT = []

# converts the encoded string into a list of individual characters
CHARACTER_LIST = list(encoded_string)

LENGTH = len(encoded_string)

# plaintext - method to decode an encoded string 
# input - encoded string (Read encoding rules above)
# output - decoded string 
def plaintext(encoded_string):

	i = 0

	# loops through length of list while i is less than list length
	while i < LENGTH:
		
		# checks if character at index i is a digit
	 	if CHARACTER_LIST[i].isdigit() == True:
	 		
	 		number_of_skips = CHARACTER_LIST[i]

	 		# checks if character at index (i + 1) is a digit
	 		if LENGTH >= 1 and CHARACTER_LIST[i + 1].isdigit() == True:

	 			plaintext_multidigit(encoded_string)

	 			print "The decoded string taking multidigits into account is: " + "\"" + ''.join(DECODED_WORD_MULTIDIGIT) + "\""
	 			
	 			# breaks out of while loop if multigit method has run
	 			break
	 			
	 		# total number of characters to skip
	 		i = i + int(number_of_skips) + 1

	 		if i > LENGTH:
	 			
	 			print "The string is not properly encoded"
	 			
	 			break

	 		# appends the character to the running decoded string
	 		DECODED_WORD.append(CHARACTER_LIST[i])

	 	i += 1

	print "The decoded string is: " + "\"" + ''.join(DECODED_WORD) + "\""
	#print "The decoded string taking multidigits into account is: " + "\"" + ''.join(DECODED_WORD_MULTIDIGIT) + "\""


# plaintext_multidigit - a method that runs only if first two characters in encoded string are digits
# input - encoded string
# output - decoded string taking multidigits into account
def plaintext_multidigit(encoded_string):

	i = 0

	while i < LENGTH:

		if CHARACTER_LIST[i].isdigit() == True:

			number_of_skips_multidigit = int(''.join(CHARACTER_LIST[i] + CHARACTER_LIST[i + 1]))

			i = i + int(number_of_skips_multidigit) + 2

			if i > LENGTH:
	 			print "i is greater than length"
	 			break
	 				
	 		# appends the character to the running decoded alt string
	 		DECODED_WORD_MULTIDIGIT.append(CHARACTER_LIST[i])
	 	
	 	i += 1



plaintext(encoded_string)




