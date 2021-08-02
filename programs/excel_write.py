import xlsxwriter

wb = xlsxwriter.Workbook('abc.xlsx')
worksheet = wb.add_worksheet()
worksheet.write('A1', 'Test Story')
worksheet.write('B1', 'Test Case ID')
worksheet.write('C1', 'Test Case Name')

column = 0
row = 1
content = ["Login", "Search course", "Select course", "Payment"]
for i in content:
    worksheet.write(row, column, i)
    row = row + 1
wb.close()
