"""
Given two arrays a[] and b[] respectively of size n and m, the task is to print the count of elements in the
intersection (or common elements) of the two arrays.

For this question, the intersection of two arrays can be defined as the set containing distinct common elements
between the two arrays.

Example 1:

Input:
n = 5, m = 3
a[] = {89, 24, 75, 11, 23}
b[] = {89, 2, 4}

Output: 1

Explanation:
89 is the only element
in the intersection of two arrays.

Example 2:

Input:
n = 6, m = 5
a[] = {1, 2, 3, 4, 5, 6}
b[] = {3, 4, 5, 6, 7}

Output: 4

Explanation:
3 4 5 and 6 are the elements
in the intersection of two arrays.

Expected Time Complexity: O(n + m).
Expected Auxiliary Space: O(min(n,m)).
"""


def intersection(arr1, arr2):
    d = {}
    result = []
    for ele in arr1:
        if ele not in d:
            d[ele] = 1
        else:
            d[ele] += 1

    for ele in arr2:
        if ele in d:
            result.append(ele)

    return result






