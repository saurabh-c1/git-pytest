"""
Program :- Find a factorial

Steps :-
        1) Enter number
        2) Iterate over the length of the input
        3) Multiply by i
"""
import time


class Factorial:

    def factorial(num):

        print(num, end=" x ")

        for i in range(num - 1, 1, -1):
            print(i, end=" x ")
            num = num * i

        print("1 = ", num)
        return num


fact = Factorial
num = int(input("Enter number to find factorial :- "))
print("\nFactorial of {} = {}".format(num, fact.factorial(num)))
