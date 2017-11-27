import collections

def string_compression(str1):
	char_count = collections.OrderedDict()
	for char in str1:
		if char in char_count:
			char_count[char] = char_count[char] + 1
		else:
			char_count[char] = 1
	new_string = ''
	for char, count in char_count.items():
		compressed = '{}{}'.format(char, count)
		new_string += compressed
	return new_string

if __name__ == '__main__':
	print(string_compression('AAAABBBBCCCCCDDEEEE'))
	print(string_compression('AAABCCDDDDD'))