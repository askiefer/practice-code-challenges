
def unique_pairs_amt(lst, k):
	if not lst or len(lst) < 2:
		return

	seen = set()
	output = set()

	for num in lst:
		target = k-num
		if target not in seen:
			seen.add(num)
		else:
			output.add( (min(num,target),  max(num,target)) )

# uses O^2 time, not ideal
def unique_pairs(lst, k):
	if not lst or len(lst) < 2:
		return

	pairs = []
	for num in lst:
		lst.pop(0)
		for val in lst:
			if k == num + val:
				pair = sorted([num, val])
				if pair not in pairs:
					pairs.append(pair)
	return pairs

if __name__ == "__main__":
	print(unique_pairs([4, 2, 7, 2, 1], 9))
	print(unique_pairs([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10))
	print(unique_pairs([1,2,2,2,3], 4))