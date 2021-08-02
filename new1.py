import re

file = open("sample.txt", "w")
file.write("First Line\nSecond Line\nThird Line")
file.close()
file = open("sample.txt", "r")
pattern = "Second"
for i in file:
    if re.search(pattern, i):
        print(i)
