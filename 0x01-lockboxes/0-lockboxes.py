#!/usr/bin/python3
def canUnlockAll(boxes):

    # Set to keep track of unlocked boxes
    unlocked_boxes = set([0])

    # Function to perform depth-first search
    def dfs(box_index):

        for key in boxes[box_index]:
            if key not in unlocked_boxes:
                unlocked_boxes.add(key)
                dfs(key)

    # Start DFS from the first box
    dfs(0)

    # Check if all boxes are unlocked
    return len(unlocked_boxes) == len(boxes)
    
