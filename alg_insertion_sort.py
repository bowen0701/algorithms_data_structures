from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def insertion_sort(a_list):
    """Insertion Sort algortihm.

    Time complexity: O(n^2).
    """
    gen = ((i, v) for i, v in enumerate(a_list) if i > 0)
    for (i, v) in gen:
        pos = i
        while pos > 0 and a_list[pos - 1] > v:
            a_list[pos] = a_list[pos - 1]
            pos -= 1
        a_list[pos] = v


def main():
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insertion_sort(a_list)
    print(a_list)


if __name__ == '__main__':
    main()
