from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


"""Make Change.

Compute how many distinct ways you can make change that amount.
Assume that you have an infinite number of each kind of coin.
"""


def make_change_recur(amount, coins):
    """Make change by recursion.

    Time complexity: O(2^n).
    Space complexity: O(1).
    """
    if amount < 0:
        return 0
    if amount == 0:
        return 1

    # When number of coins is 0 but there is still amount remaining.
    n = len(coins)
    if n <= 0 and amount >= 1:
        return 0

    return (make_change_recur(amount - coins[n - 1], coins)
            + make_change_recur(amount, coins[:(n - 1)]))


def _make_change_memo(amount, coins, T):
    """Helper function for make_change_memo()."""
    if amount == 0:
        return 1
    if amount < 0:
        return 0

    n = len(coins)
    if n <= 0 and amount >= 1:
        return 0

    counter_in = _make_change_memo(amount - coins[n - 1], coins, T)
    counter_out = _make_change_memo(amount, coins[:(n - 1)], T)
    T[n - 1][amount] = counter_in + counter_out

    return T[n - 1][amount]


def make_change_memo(amount, coins):
    """Make change by top-bottom dynamic programming: 
    recursion + memoization."""
    n = len(coins)
    T = [[0] * (amount + 1) for c in range(n)]

    for c in range(n):
        T[c][0] = 1

    return _make_change_memo(amount, coins, T)


def make_change_dp(amount, coins):
    """Make change by bottom-up dynamic programming."""
    pass


def main():
    import time

    amount = 5
    coins = [1, 2, 3]    # Ans = 5.

    start_time = time.time()
    print('Make change by recursion: {}'
          .format(make_change_recur(amount, coins)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('Make change by memo: {}'
          .format(make_change_memo(amount, coins)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
