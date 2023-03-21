import mysql.connector, openpyxl

# myconn = mysql.connector.connect(host = "localhost", user = "root",
# passwd = "19072002hoangnunnnnn", database = "pythondb")
# cur = myconn.cursor()
# sql = ("insert into students(masv, ho, ten, ngaysinh, toan, ly, hoa) "
# + "values (%s, %s, %s, %s, %s, %s, %s)")
# # val = ("masv1", "hoang","11-04-2002", 5.1, 7.5,3.3)

# wb = openpyxl.load_workbook("input.xlsx")
# # print(wb.sheetnames)
# ws = wb[wb.sheetnames[0]]
# for i in range(12, 63):
#     # print(ws.cell(row=i, column=2).value)
#     val = (ws.cell(row=i, column=2).value, ws.cell(row=i, column=3).value, ws.cell(row=i, column=4).value, ws.cell(row=i, column=5).value, ws.cell(row=i, column=6).value, ws.cell(row=i, column=7).value, ws.cell(row=i, column=8).value)
#     try:
#         cur.execute(sql,val)
#         myconn.commit()
#     except:
#         myconn.rollback()
# # print(cur.rowcount,"record inserted!")
# myconn.close()

myconn = mysql.connector.connect(host = "localhost", user = "root",
passwd = "19072002hoangnunnnnn", database = "pythondb")
#tạo đối tượng cursor
cur = myconn.cursor()
try:
# select dữ liệu từ database
    cur.execute("SELECT * FROM sv")
# tìm nạp các hàng từ đối tượng con trỏ 
    result = cur.fetchall()
    for x in result:
        print(x); 
except:
    myconn.rollback()
    myconn.close()