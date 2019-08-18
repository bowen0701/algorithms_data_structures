"""Leetcode 72. Edit Distance
Hard

URL: https://leetcode.com/problems/edit-distance/

Given two words word1 and word2, find the minimum number of operations 
required to convert word1 to word2.

You have the following 3 operations permitted on a word:
- Insert a character
- Delete a character
- Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int

        Time complexity: O(n1*n2).
        Space complexity: O(n1*n2).
        """
        # Apply dynamic programming with table T.
        n1, n2 = len(word1), len(word2)

        T = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        for j in range(n2 + 1):
            T[0][j] = j

        for i in range(n1 + 1):
            T[i][0] = i

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                # Compare current chars's diff for replace.
                if word1[i - 1] == word2[j - 1]:
                    diff = 0
                else:
                    diff = 1

                # Compute min of delete, insert and replace.
                T[i][j] = min(T[i - 1][j] + 1, 
                              T[i][j - 1] + 1, 
                              T[i - 1][j - 1] + diff)

        return T[-1][-1]


def main():
    # Ans: 3.
    word1 = "horse"
    word2 = "ros"
    print Solution().minDistance(word1, word2)

    # Ans: 5.
    word1 = "intention"
    word2 = "execution"
    print Solution().minDistance(word1, word2)


if __name__ == '__main__':
    main()
