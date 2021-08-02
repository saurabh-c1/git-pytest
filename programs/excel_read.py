import xlrd

path = "abc.xlsx"
wb = xlrd.open_workbook(path)
print("Number of sheet :-", wb.nsheets)
print("Sheet Name :- ", wb.sheet_names())
sheet = wb.sheet_by_index(0)
row = sheet.nrows
col = sheet.ncols
print("--" * 50)
print("Number of rows = {},\nNumber of columns = {} ".format(row, col))
print("--" * 50)
for i in range(col):
    print(sheet.col(i))
print("--" * 50)
for j in range(1, row):
    print(sheet.row(j))
