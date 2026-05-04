def is_palindrome(self, s: str) -> bool:
    """
    Checks if a string is a valid palindrome considering only alphanumeric characters.

    Args:
        s (str): Input string.

    Returns:
        bool: True if palindrome, False otherwise.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    left, right = 0, len(s) - 1

    while left < right:
        # skip non-alphanumeric
        while left < right and not s[left].isalnum():
            left += 1

        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True
