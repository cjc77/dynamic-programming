#! usr/bin/env python3

"""
Use Dynamic Programming to solve "take-it-or-leave-it" kanpsack problem.

Given weights/values - how to pick items to maximize sum of value while weight <= knapsack weight.
"""

import sys

def dynamic_knapsack(W, wt, val):
    """
    Find optimal arrangement <= W.

    Extra row @ top created to hold 0s. Removed @ return.
    """
    rows = len(wt) + 1
    cols = W + 1
    # Create empty Matrix
    T = [[0] * cols for i in range(rows)]
    for row in range(1, rows):
        for col in range(1, cols):
            if col < wt[row - 1]:
                T[row][col] = T[row - 1][col]
            else:
                # need to use val[row - 1] and wt[row - 1] because of added row of 0s
                T[row][col] = max(T[row - 1][col], val[row - 1] + T[row - 1][col - (wt[row - 1])])

    return T[-1][-1]


def main():
    inp = sys.stdin.read().split('\n')
    l1, l2, l3 = inp[0], inp[1], inp[2]
    W = int(l1)
    wt = [int(idx) for idx in l2.split()]
    val = [int(idx) for idx in l3.split()]

    # print(W, wt, val)
    solution = dynamic_knapsack(W, wt, val)
    print(solution)

if __name__ == '__main__':
    main()
