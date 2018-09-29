'''Program 'hamming-extra.py' to take an n-bit input in hexadecimal and generate and print its hamming code, where n is any positive integer, by Anway De   10/10/17'''

import math

def hamming(value):
	'''Function to find the hamming code of a hexadecimal input. Takes a hexadecimal integer as argument, returns a string form of a hexadecimal number'''

	storedbits = store_bits(value)

	index = 0

	while 2**index <= len(storedbits):											#traverses the parity bits

		count = 0																#count holds the number of 1s in the positions the parity bit checks

		for i in range(len(storedbits)):										#traverses the entire list
			if ((i+1) >> index) & 1:											#the parity bit at position 2^i checks those indexes of the list whose (i+1)th digit from the left in their binary representations is a 1
				if storedbits[i] == 1:
					count += 1

		storedbits[(2**index)-1] = count%2										#parity bit set to 1 if number of 1s is odd, set to 0 if number of 1s is even
		index += 1

	'''Reconstructing the number from the bits stored in the list'''
	num = ''

	for i in storedbits:
		num += str(i)

	num = int(num, 2)

	return hex(num)[2:]															#Omitting the '0x' from the returning string

def store_bits(val):
	'''Function to extract the bits from the hexadecimal input and store them in a list'''

	ham_len = int(len(bin(val))-1+int(math.log2(len(bin(val)))))				#determines the length of the hamming code depending on the length of the input
	ham_list = []
	dig_pos = len(bin(val))-2													#getting the number of bits by ommitting '0b'

	for i in range(ham_len):
		if int(math.log2(i+1))==math.log2(i+1):
			ham_list.append(None)												#assigning None to the parity bit positions
		else:
			dig_pos -= 1
			ham_list.append((val >> dig_pos) & 1)								#extracting the bits

	return ham_list

def take_input():
	'''Function to take a correct input in hexadecimal'''

	n = input("Enter a number in hexadecimal to generate the hamming code:  ")
	while True:
		try:
			val = int(n, 16)
			break
		except:
			n = input("Incorrect input. Try again. \nEnter a number in hexadecimal:  ")

	return val

#main

print("****HAMMING CODE GENERATOR****\n")
print("This program generates the hamming code for any hexadecimal number that you input.\n")

value = take_input()
hamming_code = hamming(value)

print ("The hamming code is", hamming_code)