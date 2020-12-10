# encoding = utf-8
from tkinter import *

import mariadb

textString = ""
root = Tk()
root.title("sql tool")
frame = Frame(root)
data_frame = Frame(root)
frame.pack(side=TOP)
data_frame.pack(side=BOTTOM)


def excutesql():
    connect_params = {
        'user': 'debianmysql',
        'password': 'debianmysqlpasswd',
        'host': '172.21.48.116',
        'port': 3306,
        'database': 'mysqltest'
    }
    db = mariadb.connect(**connect_params)
    cursor = db.cursor()
    sql = var.get()
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        print(cursor.rowcount)
        height = cursor.rowcount + 1
        width = len(cursor.description)
        field_names = [i[0] for i in cursor.description]
        field_values = [field_names]

        for row in results:
            values = []
            for value in row:
                values.append(value)
            field_values.append(values)
        print(field_values)

        for i in range(height):
            for j in range(width):
                addr = StringVar(value=field_values[i][j])
                b = Entry(data_frame, textvariable=addr)
                b.grid(row=i, column=j)

    except:
        print("Error: unable to fetch data")
        db.close()


label = Label(frame, text="sql to execute")
label.pack(side=LEFT)
var = StringVar()
input_sql = Entry(frame, width=80, textvariable=var)
input_sql.pack(side=LEFT)

excutesqlbutton = Button(frame, text="execute", command=excutesql)
excutesqlbutton.pack(side=LEFT)

root.mainloop()
