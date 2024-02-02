#!/usr/bin/python3
'''py'''


def canUnlockAll(boxes):
    """checks if alll boxes can be opened
    """
    items = len(boxes)
    clés = set()
    op_boxe = []
    i = 0

    while i < items:
        oldi = i
        op_boxe.append(i)
        clés.update(boxes[i])
        for clé in clés:
            if clé != 0 and clé < items and clé not in op_boxe:
                i = clé
                break
        if oldi != i:
            continue
        else:
            break

    for i in range(items):
        if i not in op_boxe and i != 0:
            return False
    return True