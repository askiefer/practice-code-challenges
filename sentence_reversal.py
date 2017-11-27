
def sentence_reversal(strg):
	# remove the whitespace before and after the string
	strg = strg.strip()
	# split the string on each space
	lst = strg.split(' ')
	new_lst = []
	for word in lst:
		if word == '':
			continue
		new_lst.insert(0, word)
	return ' '.join(new_lst)

if __name__ == '__main__':
	print(sentence_reversal('   Hello John    how are you   '))
	print(sentence_reversal('    space before'))