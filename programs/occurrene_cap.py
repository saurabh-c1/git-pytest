"""
Program :-  Find the count of Capital and Small letters in a string

Steps :-
        1) Enter input string
        2) Using for loop iterate the string
        3) Use isupper(), islower()
        4) Print the count
"""


class FindUpperLower:
    def find_cap_small(s):
        cnt_cap = 0
        cnt_low = 0
        for i in range(len(s)):
            if s[i].isupper():
                cnt_cap = cnt_cap + 1
            elif s[i].islower():
                cnt_low = cnt_low + 1
        print("Input String = {} ".format(s))
        print("Upper Case letter = {} ".format(cnt_cap))
        print("Lower Case letter = {} ".format(cnt_low))


cs = FindUpperLower
s = input("Enter the string :- ")
cs.find_cap_small(s)

