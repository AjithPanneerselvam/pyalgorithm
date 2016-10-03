"""
Bubble sort
Time Complexity - O(n^2)
Space Complexity - O(n)
"""

def sort(ls):

    flag = True

    for i in range(len(ls)):
        # Flag helps to break the loop, when the list is sorted
        if flag == False:
            break
        flag = False

        for j in range(len(ls)-1):
            if ls[j] > ls[j+1]:
                ls[j],ls[j+1] = ls[j+1],ls[j]
                flag = True
