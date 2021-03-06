"""Leetcode 1054. Distant Barcodes
Medium

URL: https://leetcode.com/problems/distant-barcodes/

In a warehouse, there is a row of barcodes,
where the i-th barcode is barcodes[i].

Rearrange the barcodes so that no two adjacent barcodes are equal.
You may return any answer, and it is guaranteed an answer exists. 

Example 1:
Input: [1,1,1,2,2,2]
Output: [2,1,2,1,2,1]

Example 2:
Input: [1,1,1,1,2,2,3,3]
Output: [1,3,1,3,2,1,2,1]

Note:
- 1 <= barcodes.length <= 10000
- 1 <= barcodes[i] <= 10000
"""

class SolutionDictSort(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]

        Time complexity: O(n*logn).
        Space complexity: O(n).
        """
        from collections import defaultdict

        # Use dict to count barcode's number.
        barcode_num_d = defaultdict(int)
        for b in barcodes:
            barcode_num_d[b] += 1

        # Starting from pos 0, fill barcodes at even positions.
        # Then starting from position 1, odd position.
        res = [0] * len(barcodes)
        pos = 0

        for b, n in sorted(barcode_num_d.items(), 
                           key=lambda x: x[1], reverse=True):
            while n:
                res[pos] = b
                pos += 2
                n -= 1

                # If position is out of boundary, start from position 1.
                if pos >= len(barcodes):
                    pos = 1

        return res


class SolutionDictMost(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]

        Time complexity: O(n).
        Space complexity: O(n).
        """
        from collections import defaultdict

        # Use dict to count barcode's number.
        barcode_num_d = defaultdict(int)
        for b in barcodes:
            barcode_num_d[b] += 1

        # Get the most popular barcode.
        most_b, most_n = 0, 0
        for (b, n) in barcode_num_d.items():
            if n > most_n:
                most_b, most_n = b, n

        # Fill the most popular barcode at even positions.
        res = [0] * len(barcodes)
        pos = 0
        while most_n:
            res[pos] = most_b
            pos += 2
            most_n -= 1

        # Fill the remaining barcodes at the following even to odd positions.
        for (b, n) in barcode_num_d.items():
            if b != most_b:
                while n:
                    # If position is out of boundary, start from position 1.
                    if pos >= len(barcodes):
                        pos = 1

                    res[pos] = b
                    pos += 2
                    n -= 1

        return res


def main():
    # Output: [2,1,2,1,2,1]
    barcodes = [1,1,1,2,2,2]
    print 'By dict+sort', SolutionDictSort().rearrangeBarcodes(barcodes)
    print 'By dict+most', SolutionDictMost().rearrangeBarcodes(barcodes)

    # Output: [1,3,1,3,2,1,2,1]
    barcodes = [1,1,1,1,2,2,3,3]
    print 'By dict+sort', SolutionDictSort().rearrangeBarcodes(barcodes)
    print 'By dict+most', SolutionDictMost().rearrangeBarcodes(barcodes)


if __name__ == '__main__':
    main()
