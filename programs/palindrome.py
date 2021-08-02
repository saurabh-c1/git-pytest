"""
Program :- To find if the given input is palindrome

Steps :-
        1) Take input
        2) Reverse the input
        3) If reversed input matches with original input then it is Palindrome
"""


class Palindrome:
    def find_palindrome(self, num):
        rev = num[::-1]
        if rev == num:
            print("Entered input is Palindrome...!")
        else:
            print("Entered input is not a Palindrome...!")


p = Palindrome()
num = input("Enter the number / string to check for Palindrome :- ")
p.find_palindrome(num)
