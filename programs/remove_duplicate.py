"""
Program :-  Remove duplicate characters from string

Steps :-
        1) Enter input string
        2) Take the temporary string as empty because string is immutable
        3) Iterate over original string length and find add distinct element into new string
"""


class RemoveDuplicate:
    def remove_duplicate(s):
        temp = ""
        for i in range(len(s)):
            c = s[i]
            if c not in temp:
                temp = temp + c
        print(temp)


rd = RemoveDuplicate
s = input("Enter string :- ")
rd.remove_duplicate(s)
