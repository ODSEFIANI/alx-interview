#!/usr/bin/python3
from collections import Counter


def canUnlockAll(boxes):

    list1 = list(range(0, len(boxes)))
    print(list1)
    list2 = []
    locked = []
    match = []
    duplicates = []

    for index, box in enumerate(boxes):
        for value in box:
            list2.append(value)

            # Check if the value is equal to the box number
            if value == index:
                match.append(value)

    # Count occurrences of each value in list2
    counter = Counter(list2)

    # Find duplicates in list2
    duplicates = [item for item, count in counter.items() if count > 1]

    # Check if all elements in match are also duplicates
    for value in match:
        if value not in duplicates:
            return False

    # Check for locked boxes
    for elem in list2:
        if elem not in list1:
            locked.append(elem)

    # Check if all boxes can be opened
    if len(locked) == 0:
        return True
    else:
        return False
