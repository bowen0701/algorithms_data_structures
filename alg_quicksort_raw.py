from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def _partition(a_list, first, last):
    """Get split point for patition."""
    # pivot_pos = _select_pivot_value(a_list, first, last)
    # pivot_value = a_list[pivot_pos]
    pivot_value = a_list[first]
    
    left_mark = first + 1
    right_mark = last

    done_bool = False
    while not done_bool:
        while (a_list[left_mark] <= pivot_value and
               left_mark <= right_mark):
            left_mark += 1

        while (a_list[right_mark] >= pivot_value and 
               right_mark >= left_mark):
            right_mark -= 1

        if right_mark < left_mark:
            done_bool = True
        else:
            temp = a_list[left_mark]
            a_list[left_mark] = a_list[right_mark]
            a_list[right_mark] = temp
            print(a_list)

    # temp = a_list[pivot_pos]
    # a_list[pivot_pos] = a_list[right_mark]
    temp = a_list[first]
    a_list[first] = a_list[right_mark]
    a_list[right_mark] = temp
    print(a_list)

    return right_mark


def _quicksort_recur(a_list, first, last):
    if first < last:
        split_point = _partition(a_list, first, last)
        _quicksort_recur(a_list, first, split_point - 1)
        _quicksort_recur(a_list, split_point + 1, last)


def quicksort(a_list):
    """Quick sort algortihm with recursion."""
    _quicksort_recur(a_list, 0, len(a_list) - 1)


def main():
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print('a_list: \n{}'.format(a_list))
    print('Quick sort: ')
    quicksort(a_list)


if __name__ == '__main__':
    main()
