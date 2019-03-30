from openpyxl import load_workbook
wb = load_workbook("D:/aaa.xlsx")
sheet1 = wb.get_sheet_by_name("损益表")
listcolumn = ["月份"]
# 遍历出表头
for index in range(2, 29):
    column = sheet1["A"+str(index)].value
    if not (column is None):
        column = column.strip()
        listcolumn.append(column)     
    else:
        listcolumn.append(column)

# print(listcolumn)

# 遍历内容
listLines = ["B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",  "W", "X", "Y", "Z", "AA"]
count = 1
for cloumn in listLines:
    insert = "insert into report_finance values ("
    for index in range(len(listcolumn)):
        if not (listcolumn[index] is None):
            columnValue = sheet1[cloumn+str(index+1)].value   
            if(index == 0):
                columnValue = "'"+str(columnValue)+"'"       
            if(columnValue is not None):
                if str(columnValue).startswith("="):
                    columnValue = None
                insert += str(columnValue) + ","
            else:
                insert += " null , "
        else:
            continue
    insert = insert.rstrip(",").rstrip(", ")+");"
    print(insert)
    count += 1