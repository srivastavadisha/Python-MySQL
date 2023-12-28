import mysql.connector
mydb=mysql.connector.connect(
    host='localhost' ,
    user='root',
    password='113008',
    database='db1'
    )
cur=mydb.cursor()
s="DELETE FROM book WHERE title='PHP'"
cur.execute(s)
mydb.commit()
