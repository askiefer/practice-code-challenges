import collections

# uses a set, but also the sorted function
# pithiest but not linear time
def unique_chars(string):
	return sorted(set(string)) == sorted(list(string))

def unique_chars_two(string):
	char_count = {}
	for char in string:
		if char in char_count:
			return False
		else:
			char_count[char] = 1
	return True

if __name__ == '__main__':
	print(unique_chars('goo'))
	print(unique_chars('abchdl'))

	print(unique_chars_two('goo'))
	print(unique_chars_two('oepwlqkf'))
	print(unique_chars_two('lwopdrp'))
