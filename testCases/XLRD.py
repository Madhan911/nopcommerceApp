import xlrd
#path = "C://Users//Nani Madhan//OneDrive//Desktop//AutomationData//testxl.xlsx"
workbook = xlrd.open_workbook("C://Users//Nani Madhan//OneDrive//Desktop//AutomationData//testxl.xlsx")
sheet = workbook.sheet_by_name("reg")

rows = sheet.nrows
cols = sheet.ncols

print(rows)
print(cols)
