import xlrd

wb = xlrd.open_workbook('salaries.xlsx')  # read xlsx file
sheet = wb.sheet_by_index(0)  # get sheet by index

# dict = [x for x in sheet.row_values(1, start_colx = 1)]

d2 = {}
for x in range(1, sheet.nrows):
    for y in range(1):
        d2[sheet.cell_value(x, 0)] = {sheet.cell_value(0, y): sheet.cell_value(x, y)}
print(d2)
# num_rows = sheet.nrows  # row len
# num_col = sheet.ncols  # colum len

# Выведите название региона с самой высокой медианной зарплатой
# через пробел, название профессии с самой высокой средней зарплатой по всем регионам.

# print(dict)  # get cell values

# for rownum in range(sheet.nrows):
#     row = sheet.row_values(rownum)
#     for cel in row:
#         print(cel)


# nmin = sh.row_values(6)[2]
# for rownum in range(7, 27):
#     temp = sh.row_values(rownum)
#     nmin = min(nmin, temp[2])
# print(nmin)
