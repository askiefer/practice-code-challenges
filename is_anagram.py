
# given two strings, check to see if they are anagrams of each other

# first implementation
def is_anagram_one(str_1, str_2):
	# remove the spaces and make capitalization lower
	# forget punctuation for now
	str1 = sorted(str_1.replace(' ', '').lower())
	str2 = sorted(str_2.replace(' ', '').lower())
	for char in str1:
		indx = str1.index(char)
		if not char == str2[indx]:
			return False
	return True

# second implementation
# use a char count dictionary and them compare them
def is_anagram_two(str_1, str_2):
	str_1 = str_1.replace(' ', '').lower()
	str_2 = str_2.replace(' ', '').lower()
	chars_1 = create_char_dict(str_1)
	chars_2 = create_char_dict(str_2)
	# basically have to do a deep equals of the two dicts
	for char, count in chars_1.items():
		if char not in chars_2:
			return False
		if chars_2[char] != count:
			return False
	return True

def create_char_dict(str_n):
	chars = {}
	for char in str_n:
		if char in chars:
			num_chars = chars.get(char)
			chars[char] = num_chars + 1
		else:
			chars[char] = 1
	return chars

if __name__ == "__main__":
	# print(is_anagram_one('dog', 'G od'))
	# print(is_anagram_one('clint eastwood', 'old west action'))
	# print(is_anagram_one('aa', 'bb'))

	# print(is_anagram_two('dog', 'G od'))
	# print(is_anagram_two('clint eastwood', 'old west action'))
	# print(is_anagram_two('aa', 'bb'))

	print(logical_xor('dog', 'G od'))
	print(logical_xor('clint eastwood', 'old west action'))
	print(logical_xor('aa', 'bb'))
