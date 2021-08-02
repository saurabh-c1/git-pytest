"""
Program :- To reverse the list elements
           Perform sort operation

Steps :-
        1)
        2)
        3)
        4)
"""


def reverse_list(lis1, lis2):
    for i in lis1[::-1]:
        lis2.append(i)
        print("Inside loop :- ", lis2)
    return lis2


def sort_list(lis1):
    for i in range(len(lis1)):
        for j in range(0, len(lis1)-1):
            if lis1[j] > lis1[j + 1]:
                lis1[j], lis1[j + 1] = lis1[j + 1], lis1[j]
    return lis1


lis1 = [1, 4, 3, 2, 5]
lis2 = []
reverse_list(lis1, lis2)
sort_list(lis1)
print("Reversed list is :- ", lis2)
print("Sorted list is :- ", lis1)