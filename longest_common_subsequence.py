#! usr/bin/env python3

import sys

def find_longest_common_subseq(string1, string2):
    """
    Find longest common subsequence of string1 and string2
    """
    rows = len(string2) + 1
    cols = len(string1) + 1

    table = [[0] * cols for _ in range(rows)]

    for r in range(1, rows):
        for c in range(1, cols):
            previous_best = max(table[r - 1][c], table[r][c - 1], table[r - 1][c - 1])
            if string2[r - 1] != string1[c - 1]:
                table[r][c] = previous_best
            else:
                table[r][c] = previous_best + 1

    for line in table:
        print(line)


def main():
    inp = sys.stdin.read().split()
    string1, string2 = inp[0], inp[1]
    find_longest_common_subseq(string1, string2)

if __name__ == '__main__':
    main()
