import mysql.connector
mydb=mysql.connector.connect(
    host='localhost' ,
    user='root',
    password='113008',
    database='db1'
    )
cur=mydb.cursor()
s="INSERT INTO book (bookid,title,price) VALUES(%s,%s,%s)"
books=[(2, 'PHP', 135),(3,'Java8',450),(4,'HTML',200)]
cur.executemany(s,books)
mydb.commit()
