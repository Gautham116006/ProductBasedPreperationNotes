"""
Given a binary array A[] of size N. The task is to arrange the array in increasing order.

Note: The binary array contains only 0  and 1.

Example 1:

Input:
N = 5
A[] = {1,0,1,1,0}
Output: 0 0 1 1 1

Example 2:

Input:
N = 10
A[] = {1,0,1,1,1,1,1,0,0,0}
Output: 0 0 0 0 1 1 1 1 1 1
"""


def sort_binary_arr(arr):
    i = 0
    j = len(arr) - 1

    while i < j:
        if arr[i] == 1 and arr[j] == 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        elif arr[j] == 1:
            j -= 1
        elif arr[i] == 0:
            i += 1

    return arr


print(sort_binary_arr([1, 1, 1, 1, 1, 0]))
