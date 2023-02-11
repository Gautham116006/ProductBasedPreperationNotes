"""
Given two sorted arrays A and B of size M and N respectively. Each array may have some elements in common with the other
array. Find the maximum sum of a path from the beginning of any array to the end of the two arrays.
We can switch from one array to another array only at the common elements.Both the arrays are sorted.
Note: Only one repeated value is considered in the valid path sum.

Example 1:

Input:
M = 5, N = 4
A[] = {2,3,7,10,12}
B[] = {1,5,7,8}
Output: 35
Explanation: The path will be 1+5+7+10+12
= 35.

Input:
M = 3, N = 3
A[] = {1,2,3}
B[] = {3,4,5}
Output: 15
Explanation: The path will be 1+2+3+4+5=15.
"""


def max_sum_path(arr1, arr2):
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] > arr2[j]:
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            break
    return max(sum(arr1[i:]), sum(arr2[j:])) + max(sum(arr1[:i]), sum(arr2[:j]))


print(max_sum_path([1, 2, 3], [3, 4, 5]))
