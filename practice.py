
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

def print_recursively(lst):
    """Prints a list recursively

    >>> print_recursively([1, 2, 3])
    1
    2
    3
    
    >>> print_recursively([])
    0
    """
    if not lst:
        return 0
    
    print lst[0]
    print_recursively(lst[1:])

# def recursive_index(needle, haystack):
#     """Find the index of an item in a list using recursion.

#     >>> recursive_index("hey", ["hey", "there", "you"])
#     0

#     >>> recursive_index("cat", ["hey", "there", "you"])
#     None
#     """
    ## FIX ME 

def binary_search(val):
    """Using binary search, return the num of guesses it will take to guess the val given

    >>> binary_search(50)
    1

    >>> binary_search(25)
    2
    """
    assert 0 < val < 101
    
    num_guesses = 0
    min_guess = 0
    max_guess = 101
    guess = None


    while guess != val:
        num_guesses += 1
        guess = (max_guess - min_guess) / 2 + min_guess

        if guess > val:
            max_guess = guess
        elif guess < val:
            min_guess = guess

    return num_guesses



