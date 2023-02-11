"""
You are given an array A, of N elements. Find minimum index based distance between two elements of the array,
x and y such that (x!=y).

Example 1:

Input:
N = 4
A[] = {1,2,3,2}
x = 1, y = 2
Output: 1
Explanation: x = 1 and y = 2. There are
two distances between x and y, which are
1 and 3 out of which the least is 1.

Example 2:

Input:
N = 7
A[] = {86,39,90,67,84,66,62}
x = 42, y = 12
Output: -1
Explanation: x = 42 and y = 12. We return
-1 as x and y don't exist in the array.
"""


def min_distance(arr, x, y):
    prev_index = None
    elements = [x, y]
    min_distance = len(arr) + 1

    for i in range(len(arr)):
        if arr[i] in elements:
            if prev_index is None:
                prev_index = i
            elif arr[i] is not arr[prev_index]:
                min_distance = min(min_distance, i - prev_index)
            else:
                prev_index = i

    if min_distance < len(arr):
        return min_distance
    else:
        return -1


print(min_distance([1, 1, 1, 1], 1, 1))
