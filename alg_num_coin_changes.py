"""Number of Coin Changes.

Count how many distinct ways you can make change that amount.
Assume that you have an infinite number of each kind of coin.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def _change_recur(amount, coins, n):
    """Helper function for num_coin_changes_recur()."""
    # Base cases.
    if amount < 0:
        return 0
    if amount == 0:
        return 1

    # When number of coins is 0 but there is still amount remaining.
    if n <= 0 and amount > 0:
        return 0

    # Sum num of ways with coin n included & excluded.
    n_changes = (_change_recur(amount - coins[n - 1], coins, n)
                 + _change_recur(amount, coins, n - 1))
    return n_changes


def num_coin_changes_recur(amount, coins):
    """Number of coin changes by recursion.

    Time complexity: O(2^n), where n is number of coins.
    Space complexity: O(1).
    """
    n = len(coins)
    return _change_recur(amount, coins, n)


def _change_memo(amount, coins, T, n):
    """Helper function for num_coin_changes_memo()."""
    # Base cases.
    if amount < 0:
        return 0
    if amount == 0:
        return 1

    if n <= 0 and amount > 0:
        return 0

    # Apply memoization.
    if T[n][amount]:
        return T[n][amount]

    # Sum num of ways with coin n included & excluded.
    T[n][amount] = (_change_memo(amount - coins[n - 1], coins, T, n)
                    + _change_memo(amount, coins, T, n - 1))

    return T[n][amount]


def num_coin_changes_memo(amount, coins):
    """Number of coin changes by top-down dynamic programming:
    recursion + memoization.

    Time complexity: O(a*n), where a is amount, and n is number of coins.
    Space complexity: O(a*n).
    """
    # Apply top-down DP with memoization tabular T: (n+1)x(amount+1).
    n = len(coins)
    T = [[0] * (amount + 1) for c in range(n + 1)]

    # For amount 0, set T[c][0] equal 1.
    for c in range(1, n + 1):
        T[c][0] = 1

    return _change_memo(amount, coins, T, n)


def num_coin_changes_dp(amount, coins):
    """Number of coin changes by bottom-up dynamic programming.

    Time complexity: O(a*n), where a is amount, and n is number of coins.
    Space complexity: O(a*n).
    """
    # Apply bottom-up DP with memoization tabular T: (n+1)x(amount+1).
    n = len(coins)
    T = [[0] * (amount + 1) for c in range(n + 1)]

    # For amount 0, set T[c][0] equal 1.
    for c in range(1, n + 1):
        T[c][0] = 1

    for c in range(1, n + 1):
        for a in range(1, amount + 1):
            if coins[c - 1] <= a:
                # If can change, sum num of ways with coin n included & excluded.
                T[c][a] = T[c][a - coins[c - 1]] + T[c - 1][a]
            else:
                # Cannot make a change by coin c.
                T[c][a] = T[c - 1][a]

    return T[-1][-1]


def main():
    import time

    # Ans = 5.
    amount = 5
    coins = [1, 2, 3]

    start_time = time.time()
    print('By recursion: {}'
          .format(num_coin_changes_recur(amount, coins)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By memo: {}'
          .format(num_coin_changes_memo(amount, coins)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By DP: {}'
          .format(num_coin_changes_dp(amount, coins)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
