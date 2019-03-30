from openpyxl import load_workbook

wb = load_workbook("aaa.xlsx")
sheet1 = wb.get_sheet_by_name("Sheet1")
listcolumn = ["月份"]

listLines = ["B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q"]
count = 1
for cloumn in listLines:
    insert = "insert into report_finance values ("
    for index in range(17):
        columnValue = sheet1[cloumn+str(index+1)].value 
        insert += str(columnValue) + ","
    insert = insert.rstrip(",").rstrip(", ")+");"
    print(insert)
