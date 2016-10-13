"""This program takes an encoded string and decodes it. The string is encoded accordingly: digits \
and other characters are added before each true character. The digits correspond to the number of \
characters to skip before finding the next true character. Then it prints the decoded string"""

# BRAINSTORMING:

# create an encoded string of characters
# create something to store the true characters once found
# create a program that takes that encoded string and decodes it:
	# turn that string into a list of characters
	# while the position of current character is less than or equal to length of encoded string
		# go through list, whenever there is a digit, skip that many ahead
		# save / store that character
		# find the next number, skip that many characters
		# print the character after that, repeat
		# continue until reaching the end of the string
	# turn the list of stored characters into a string
	# print the decoded word


# PSEUDOCODE:

# 1. Define an encoded string
# 2. Create an empty list to store decoded characters
# 3. Define a function called plaintext that takes one parameter, the encoded string
		# Convert encoded string to list form
		# Define 'length' variable
		# Set i to 0 to start incrementing through character list
		# While i is less than the length of the encoded string
			# If the character is a digit
				# Set the number of skips equal to the character at current index
				# Reset i to itself plus number of skips plus 1
				# If i is greater than the length of encoded string
					# Print 'The string is not properly encoded'
					# Break out of while loop
				# Append the character found at current index to running decoded list
			# Increment i to continue looping through encoded string
		# Print 'The decoded string is: ' plus quotations plus the joined decoded list


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




