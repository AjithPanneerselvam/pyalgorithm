"""
Selection sort
Time Complexity - O(n^2)
Space Complexity - O(n)
"""

def sort(ls):

    dest = len(ls)
    flag = True

    for i in range(len(ls)-1):
        if flag == False:
            break
        dest -= 1
        big = 0
        flag = False

        for j in range(1,dest+1):
            if ls[big] < ls[j]:
                big = j
                flag = True

        ls[big], ls[dest] = ls[dest], ls[big]
