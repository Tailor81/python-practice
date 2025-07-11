def palindrome(s):
#normalized[::-1]: This is a Python slice operation that returns the reversed version of the normalized string.
#  The [::-1] slice notation means "take the string from start to end, but step backward by 1," effectively
#  reversing the string.
    normalized = "".join(char.lower() for char in s if char.isalnum())

    return normalized == normalized[::-1]

print(palindrome("RaceCar"))
print(palindrome("Hello"))




#Comparison: The function checks if the normalized string is the same as its reverse. If they are equal, the
#  function returns True, indicating that the original string is a palindrome. If not, it returns False.