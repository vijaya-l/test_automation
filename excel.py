import xlrd

path=r"/Users/prao/downloads/Book1.xlsx"
workbook_obj=xlrd.open_workbook(path)
print(workbook_obj)

worksheet_obj=workbook_obj.sheet_by_name("data")

#get the content of all the rows--generator keywords
rows=worksheet_obj.get_rows()

#getting the value
#traversing through the generator object
for row in rows:
    print(row[0].value,row[1].value)
 
 
 
d={row[0].value:row[1].value for row in rows}