"""
Program :- Multiply elements of list 1 by same element and copy new elements in list 2

Steps :-
        1) Create list 1 and an empty list 2 []
        2) Iterate over the list 1
        3) While appending to list 2, perform multiply operation
        4) Return the list 2 and print
"""


class ListProduct:

    def lis_mul(lis1, lis2):
        for i in lis1:
            lis2.append(i * i)
        print("Inside Function:- ", lis2)
        return lis2


lis1 = [1, 2, 3, 4]
lis2 = []
lp = ListProduct
lp.lis_mul(lis1, lis2)
print("New list returned :- ", lis2)
