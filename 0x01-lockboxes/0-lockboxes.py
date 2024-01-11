#!/usr/bin/python3
"""lockboxes Interview new Challenge"""


def canUnlockAll(boxes):

    """lockboxes Interview new Challenge"""
    def dfs(box_index):
        visited.add(box_index)
        for key in boxes[box_index]:
            if key not in visited:
                dfs(key)

    n = len(boxes)
    visited = set()
    dfs(0)

    return len(visited) == n
