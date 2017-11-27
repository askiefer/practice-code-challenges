import collections

def missing_element(lst1, lst2):
	lst1.sort()
	lst2.sort()
	count = 0
	for item in lst1:
		if item != lst2[count]:
			return item
		count += 1

def missing_element_two(lst1, lst2):
	lst1.sort()
	lst2.sort()
	for num1, num2 in zip(lst1, lst2):
		if num1 != num2:
			return num1
	return False

# this is a linear solution using the XOR operator
# the XOR operation will be true if only ONE of the elements is present
def missing_element_three(lst1, lst2):
	result = 0
	for num in lst1 + lst2:
		result ^= num
	return result

if __name__ == '__main__':
	print(missing_element_three([5,5,7,7], [5,7,7]))