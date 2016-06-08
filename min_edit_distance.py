#! usr/bin/env python3

"""
Find minimum edit distance between two strings(replace, delete, add).
"""

import sys

def find_edit_distance(s1, s2):
    """
    Determine edit distance between s1 and s2.
    """
    rows = len(s2) + 1
    cols = len(s1) + 1

    T = [[0] * cols for dummy_row in range(rows)]

    # set col == s1 index + 1
    for col in range(cols):
        T[0][col] = col
    # set row == s2 index + 1
    for row in range(rows):
        T[row][0] = row

    for row in range(1, rows):
        for col in range(1, cols):
            if s2[row - 1] == s1[col - 1]:
                T[row][col] = T[row - 1][col - 1]
            else:
                T[row][col] = 1 + min(T[row][col - 1], T[row - 1][col], T[row - 1][col - 1])

    return T[-1][-1]


def main():
    inp = sys.stdin.read().split('\n')
    string1, string2 = inp[0], inp[1]
    print(find_edit_distance(string1, string2))


if __name__ == '__main__':
    main()
