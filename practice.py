
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

def count_list(lst):
    """Counts a list recursively

    >>> count_list([3, 6, 8, 2])
    4

    >>> count_list([])
    0
    """
    if not lst:
        return 0
    return 1 + count_list(lst[1:])

