from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def valid_parentheses(s):
    """Balance parentheses in a string."""
    open_close_d = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    open_set = set('([{')
    close_set = set(')]}')

    # Use stack to collect open parentheses.
    stack = []

    for c in s:
        if c in open_set:
            # If c is open parenthesis, push to stack.
            stack.append(c)
            continue
        
        if c in close_set:
            # Check if there is still open parenthesis.
            if not stack:
                return False

            # If yes, pop & compare open parenthesis and current char.
            open_c = stack.pop()
            if c != open_close_d[open_c]:
                return False

    # Check if there is still open remaining.
    if not stack:
        return True
    else:
        return False


def main():
    s = '(abcd)'  # Ans: True.
    print(valid_parentheses(s))

    s = '([(a)bcd]{ef}g)'  # Ans: True.
    print(valid_parentheses(s))

    s = '(ab{c}d]'  # Ans: False.
    print(valid_parentheses(s))


if __name__ == '__main__':
    main()
