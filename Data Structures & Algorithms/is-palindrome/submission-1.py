class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = [char for char in s if char.isalnum()]
        left = 0
        right = len(new_string) - 1
        valid = True
        while left < right:
            if new_string[left].lower() != new_string[right].lower():
                return False
            left += 1
            right -= 1
        return True