# Given an integer x, return true if x is a palindrome, and false otherwise.
#
# Example 1:
#
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
#
# Example 2:
#
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:
#
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#
# Constraints:
# -231 <= x <= 231 - 1
#
# Follow up: Could you solve it without converting the integer to a string?

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: # this will simply ignore negative numbers as they would not be categorised as palindromes
            return False
        if x == 0: # 0 is a palindrome, so we return true
            return True
        if x % 10 == 0: # if the number is divisible by 10, then it is not a palindrome
            return False
        # we reverse the number and compare it with the original number
        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x = x // 10
        if x == rev or x == rev // 10:
            return True
        return False
