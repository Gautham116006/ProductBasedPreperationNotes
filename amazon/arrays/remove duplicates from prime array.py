"""
Given an array consisting of only prime numbers, remove all duplicate numbers from it.
Input:
N = 6
A[] = {2,2,3,3,7,5}
Output: 2 3 7 5
Explanation: After removing the duplicate
2 and 3 we get 2 3 7 5.
"""


def remove_duplicates(arr):
    result = []
    d = {}

    for i in arr:
        if i not in d:
            d[i] = ""
            result.append(i)

    return result


print(remove_duplicates([2, 3, 3, 5, 5, 7]))
