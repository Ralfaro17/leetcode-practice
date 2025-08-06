def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False

    x = str(x)
    
    print(x[::-1])
    
    if x == x[::-1]:
        return True
    else:
        return False

print(isPalindrome(10))