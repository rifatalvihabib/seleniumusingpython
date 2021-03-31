import openpyxl
path="D:\Seleniumbasics\datawrite.xlsx"
workbook = openpyxl.load_workbook(path)
sheet = workbook.active
#sheet=workbook.get_sheet_by_name("sheet1") #multiple sheet

for r in range(1, 6):
    for c in range(1, 4):
        sheet.cell(row=r, column=c).value="welcome"


workbook.save(path)