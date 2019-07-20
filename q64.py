#!/usr/bin/env python
"""
Q64
"""

import itertools

N = 5


def search(maze, p1, d1, p2, d2):
    if len(p1) == len(p2):
        if p1[-1][:2] == p2[-1][:2]:
            return True
        if p1[-1][:2] == [N - 1, N - 1]:
            return False
        if p2[-1][:2] == [0, 0]:
            return False

    if p1.count(p1[-1]) > 1:
        return False

    pre = p1[-1]

    for i in range(len(dx)):
        d = (d1 - 1 + i) % len(dx)
        px = pre[0] + dx[d][0]
        py = pre[1] + dx[d][1]

        if px >= 0 and px < N and py >= 0 and py < N and maze[px + N * py] == 0:
            return search(maze, p2, d2, p1 + [[px, py, d]], d)
            break

    return False


if __name__ == '__main__':
    dx = [[1, 0], [0, -1], [-1, 0], [0, 1]]
    a = [[0, 0, -1]]
    b = [[N - 1, N - 1, -1]]
    cnt = 0

    for maze in itertools.product([0, 1], repeat=N * N - 2):
        if search([0] + list(maze) + [0], a, 3, b, 1):
            cnt += 1

    print("result =", cnt)
