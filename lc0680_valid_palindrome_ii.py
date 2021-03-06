"""Leetcode 680. Valid Palindrome II
Easy

URL: https://leetcode.com/problems/valid-palindrome-ii/

Given a non-empty string s, you may delete at most one character.
Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True

Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

Note:
The string will only contain lowercase characters a-z.
The maximum length of the string is 50000.
"""

class SolutionBrute(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool

        Note: Time Limit Exceeded

        Time complexity: O(n^2).
        Space complexity: O(n).
        """
        # Check full string.
        if s == s[::-1]:
            return True

        # Check if delete one character.
        for i in range(len(s)):
            s_partial = s[:i] + s[(i+1):]
            if s_partial == s_partial[::-1]:
                return True

        return False


class SolutionTwoPointers(object):
    def _isPalindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False

            i += 1
            j -= 1

        return True

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool

        Time complexity: O(n).
        Space complexity: O(1).
        """
        # Apply two pointers method.
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] != s[j]:
                # If there is one mismatch, skip left or right char.
                return (self._isPalindrome(s, i + 1, j)
                        or self._isPalindrome(s, i, j - 1))

            i += 1
            j -= 1

        return True


def main():
    # Output: True
    s = 'aba'
    print SolutionBrute().validPalindrome(s)
    print SolutionTwoPointers().validPalindrome(s)

    # Output: True
    s = 'abca'
    print SolutionBrute().validPalindrome(s)
    print SolutionTwoPointers().validPalindrome(s)

    # Output: False
    s = 'aacb'
    print SolutionBrute().validPalindrome(s)
    print SolutionTwoPointers().validPalindrome(s)


if __name__ == '__main__':
    main()
