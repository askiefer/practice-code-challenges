
def reverse(str):
    """Returns the reverse of a string in place

    >>> reverse("apple")
    'elppa'

    >>> reverse("cat")
    'tac'
    """

    new_str = ""
    for i in range(len(str), 0, -1):
    	new_str += str[i-1]
    return new_str


