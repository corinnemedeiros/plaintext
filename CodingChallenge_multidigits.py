encoded_string = "1uF6YHggr3A4jk09L18L0 5OKerJI0S1h 2kkH3nm3E2BBR7koHYTgRE1d!ppp"

# tested encoded strings: "2nsb0u3iohg" , "4oikem3hyea2ngd1ph4jfyya5opl91n" , \
	# "8uoplerfyc3ytho289r1ui2ttn0n5freswe" , "0i4yyhe 1dl3rr0o2ewv1re3pl2 1ty0o2wwu"

# an empty list to store found characters
DECODED_WORD = []

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

	 		# total number of characters to skip
	 		i = i + int(number_of_skips) + 1

	 		if i > length:
	 			print "The string is not properly encoded"
	 			break

	 		# appends the character to the running decoded string
	 		DECODED_WORD.append(character_list[i])

	 	i += 1

	print "The decoded string is: " + "\"" + ''.join(DECODED_WORD) + "\""

plaintext(encoded_string)