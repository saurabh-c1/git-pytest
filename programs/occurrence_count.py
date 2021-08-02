"""
Program:- To find the number of occurrences of the elements in the list.
Steps :-
        1) Create a list and pass to function
        2) Take input which element to find
        3) Iterate over the List
        4) If matching element found, increase the count
        5) Print the occurrence of an element
"""


class ElementOccurrence:
    def countX(lis, x):
        counter = 0
        for element in lis:
            if element == x:
                counter = counter + 1
        return counter


# lis = [1, 3, 4, 5, 3, 6, 6, 8, 9, 1]
lis = list(input())
x = input("Enter element to find occurrence : ")
eo = ElementOccurrence
eo.countX(lis, x)
print('--------- {} has occurred {} times ----------'.format(x, eo.countX(lis, x)))
