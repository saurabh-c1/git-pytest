def reverse(strn):
    if len(strn) == 0:
        return strn
    else:
        return reverse(strn[1:]) + strn[0]


strn = "saurabh"
print("Reverse is : ", reverse(strn))
