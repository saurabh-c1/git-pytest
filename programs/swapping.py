"""
Program :- Swap the elements without using any temporary variable

Steps :-
        1) Enter 2 elements
        2) Swap
"""


class Swapping:
    def swap(a, b):
        a = a + b
        b = a - b
        a = a - b
        print("After Swapping :: a = {} , b = {} ".format(a, b))


swp = Swapping
a = int(input("Enter first element : "))
b = int(input("Enter second element : "))
print("Before Swapping :: a = {} , b = {} ".format(a, b))
swp.swap(a, b)
