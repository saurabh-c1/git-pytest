"""
Program :- Find the occurrence of character in a string

Steps :-
        1) Enter a string
        2)
"""


class StringOccurrence:
    def find_occurrence(s, ch):
        count = 0
        for i in s:
            if i == ch:
                count = count + 1
        print("Occurrence of {} is {} times in a string : {} ".format(ch, count, s))


so = StringOccurrence
s = input("Enter the string :- ")
ch = input("Enter character :- ")
so.find_occurrence(s, ch)
